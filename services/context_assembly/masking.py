def generalize_revenue(revenue):
    if revenue < 50:
        return "0-50 Cr"
    elif revenue < 100:
        return "50-100 Cr"
    elif revenue < 150:
        return "100-150 Cr"
    else:
        return "150+ Cr"


def generalize_exposure(exposure):
    if exposure < 5:
        return "Low"
    elif exposure < 15:
        return "Medium"
    else:
        return "High"


def redact_sensitive_fields(client_data):
    client_data = client_data.copy()
    client_data.pop("tax_id", None)
    client_data.pop("account_number", None)
    return client_data
 
