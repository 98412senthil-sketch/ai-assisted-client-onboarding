import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def invoke_llm(context, retrieved_chunks):
    """
    Calls real LLM with structured prompt.
    Enforces JSON output.
    """

    prompt = f"""
You are an AI assistant helping with banking client onboarding.

Client Summary:
{context["client_summary"]}

Relevant Policy Extract:
{retrieved_chunks}

Instructions:
- Recommend suitable product(s)
- Mention maximum eligible amount
- Mention fee/interest range if available
- Provide risk commentary
- Provide confidence score between 0 and 1

Return ONLY valid JSON in this format:

{{
    "recommended_products": [],
    "max_amount": "",
    "pricing_notes": "",
    "risk_commentary": "",
    "confidence": 0.0
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
 
def safe_parse_json(response_text):
    try:
        return json.loads(response_text)
    except Exception:
        # Attempt cleanup
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        cleaned = response_text[start:end]
        return json.loads(cleaned)
