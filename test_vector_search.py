from services.knowledge_ingestion.embedding_model import EmbeddingModel
from services.knowledge_ingestion.vector_store import VectorStore

print("Loading index...")
index, metadata = VectorStore.load("sbi_vector.index", "sbi_chunks.pkl")

embedding_model = EmbeddingModel()

query = "Personal Loan maximum amount eligibility and limit"

print("Embedding query...")
query_embedding = embedding_model.embed_query(query)

print("Searching...")

results = VectorStore.search(
    index,
    query_embedding,
    metadata,
    top_k=3,
    product_filter="PERSONAL_LOAN"
)

print("\nTop Results:\n")
for r in results:
    print("----")
    print(r[:500])
 
