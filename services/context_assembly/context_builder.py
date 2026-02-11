from .masking import (
    generalize_revenue,
    generalize_exposure,
    redact_sensitive_fields
)
from .retrieval import retrieve_structured_rules


def build_context(client, rules):
    client_clean = redact_sensitive_fields(client)

    revenue_band = generalize_revenue(client["annual_revenue_cr"])
    exposure_tier = generalize_exposure(client["existing_exposure_cr"])

    structured_rules = retrieve_structured_rules(client, rules)

    context = {
        "client_summary": {
            "segment": client_clean["segment"],
            "industry": client_clean["industry"],
            "geography": client_clean["geography"],
            "risk_category": client_clean["risk_category"],
            "revenue_band": revenue_band,
            "exposure_tier": exposure_tier,
            "existing_products": client_clean["existing_products"]
        },
        "policy_summary": structured_rules
    }

    return context
 
