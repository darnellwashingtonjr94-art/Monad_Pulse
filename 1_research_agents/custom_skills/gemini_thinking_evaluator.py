import os
from google import genai

def evaluate_risk_scenario(scenario_desc: str) -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=f"Analyze tail-risk bounds for this market event: {scenario_desc}",
        config={'thinking_config': {'thinking_budget': 8192}}
    )
    return response.text
