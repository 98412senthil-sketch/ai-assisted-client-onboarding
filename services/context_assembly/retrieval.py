import json


def load_product_rules(path="data/policies/product_rules.json"):
    with open(path, "r") as f:
        return json.load(f)


def retrieve_structured_rules(client, rules):
    return rules[
        client["segment"]
    ][
        client["geography"]
    ][
        client["risk_category"]
    ]
 
