import json
from services.context_assembly.context_builder import build_context
from services.context_assembly.retrieval import load_product_rules
from services.context_assembly.precheck import pre_eligibility_check
from services.llm_gateway.llm_stub import invoke_llm
from services.decision_engine.decision_engine import final_decision

# Load sample client
with open("data/clients/sample_client.json", "r") as f:
    client = json.load(f)

# Load structured product rules
rules = load_product_rules()

# Build governed context
context = build_context(client, rules)

# Pretty print result
print(json.dumps(context, indent=2))

precheck_result = pre_eligibility_check(context)

print("\nPrecheck Result:")
print(precheck_result)

if precheck_result["decision"] == "PROCEED_TO_LLM":
    llm_output = invoke_llm(context)
    final = final_decision(precheck_result, llm_output)
else:
    final = final_decision(precheck_result)

print("\nFinal Decision:")
print(final)