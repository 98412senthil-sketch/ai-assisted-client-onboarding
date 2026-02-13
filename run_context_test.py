import json

from services.context_assembly.context_builder import build_context
from services.context_assembly.retrieval import load_product_rules
from services.context_assembly.precheck import pre_eligibility_check
from services.decision_engine.decision_engine import final_decision

# NEW imports
from services.knowledge_ingestion.vector_store import VectorStore
from services.knowledge_ingestion.embedding_model import EmbeddingModel
from services.llm_gateway.openai_client import invoke_llm, safe_parse_json

# -----------------------------
# 1. Load sample client
# -----------------------------
with open("data/clients/sample_client.json", "r") as f:
    client = json.load(f)

# -----------------------------
# 2. Load product rules (deterministic)
# -----------------------------
rules = load_product_rules()

# -----------------------------
# 3. Build governed context
# -----------------------------
context = build_context(client, rules)

print(json.dumps(context, indent=2))

# -----------------------------
# 4. Precheck (deterministic gate)
# -----------------------------
precheck_result = pre_eligibility_check(context)

print("\nPrecheck Result:")
print(precheck_result)

# -----------------------------
# 5. Conditional AI Invocation
# -----------------------------
if precheck_result["decision"] == "PROCEED_TO_LLM":

    print("\nLoading vector store...")
    index, metadata = VectorStore.load("sbi_vector.index", "sbi_chunks.pkl")

    embedding_model = EmbeddingModel()

    # Example: detect requested product (simplified for now)
    requested_product = "PERSONAL_LOAN"

    query = f"Maximum amount and eligibility for {requested_product.replace('_', ' ')}"

    print("Embedding query...")
    query_embedding = embedding_model.embed_query(query)

    print("Retrieving relevant chunks...")
    retrieved_chunks = VectorStore.search(
        index,
        query_embedding,
        metadata,
        top_k=3,
        product_filter=requested_product
    )

    print("\nRetrieved Policy Context:")
    for r in retrieved_chunks:
        print("----")
        print(r[:300])

    print("\nInvoking LLM...")
    raw_response = invoke_llm(context, retrieved_chunks)

    print("\nRaw LLM Response:")
    print(raw_response)

    llm_output = safe_parse_json(raw_response)

    print("\nParsed LLM Output:")
    print(llm_output)

    final = final_decision(precheck_result, llm_output)

else:
    final = final_decision(precheck_result)

# -----------------------------
# 6. Final Decision
# -----------------------------
print("\nFinal Decision:")
print(final)
