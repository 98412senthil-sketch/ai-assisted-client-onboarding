def final_decision(precheck_result, llm_output=None, confidence_threshold=0.75):
    decision = precheck_result["decision"]

    # If deterministic rejection
    if decision == "REJECT":
        return {
            "final_status": "REJECTED",
            "reason": precheck_result["flags"]
        }

    # If deterministic approval required
    if decision == "REQUIRES_APPROVAL":
        return {
            "final_status": "PENDING_APPROVAL",
            "reason": precheck_result["flags"]
        }

    # If LLM involved
    if decision == "PROCEED_TO_LLM" and llm_output:

        if llm_output["confidence"] < confidence_threshold:
            return {
                "final_status": "ESCALATE_FOR_REVIEW",
                "reason": "LLM confidence below threshold"
            }

        return {
            "final_status": "RECOMMEND_APPROVAL",
            "recommended_products": llm_output.get("recommended_products", []),
            "max_amount": llm_output.get("max_amount", "Not specified"),
            "pricing_notes": llm_output.get("pricing_notes", "Not specified"),
            "risk_commentary": llm_output.get("risk_commentary", ""),
            "confidence": llm_output.get("confidence", 0.0)
            }   

    return {
        "final_status": "UNDETERMINED"
    }
 
