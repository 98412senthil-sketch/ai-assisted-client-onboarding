def invoke_llm(context):
    """
    Simulated LLM invocation.
    In production, this would call Azure OpenAI / OpenAI / internal LLM.
    """

    client = context["client_summary"]
    policy = context["policy_summary"]

    response = {
        "recommended_products": policy["eligible_products"],
        "suggested_fee_range": policy["fee_range"],
        "risk_commentary": f"Client in {client['industry']} sector with {client['risk_category']} risk profile.",
        "confidence": 0.82
    }

    return response
 
