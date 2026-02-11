def pre_eligibility_check(context):
    policy = context["policy_summary"]
    client = context["client_summary"]

    flags = []
    decision = "PROCEED_TO_LLM"

    # Hard stop example: no eligible products
    if not policy.get("eligible_products"):
        decision = "REJECT"
        flags.append("No eligible products available for client segment")

    # Exposure threshold check
    if client["exposure_tier"] == "High":
        flags.append("Exposure above standard threshold — approval required")

    # Limit check
    if client["exposure_tier"] == "High" and policy.get("approval_required_above_cr"):
        decision = "REQUIRES_APPROVAL"

    return {
        "decision": decision,
        "flags": flags
    }
 
