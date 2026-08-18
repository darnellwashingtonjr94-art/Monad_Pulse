import os
from google import genai

def run_deep_quant_analysis(factor_data: str):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=f"Perform deep quantitative econometric analysis on this multi-asset order book state: {factor_data}",
        config={
            'thinking_config': {'thinking_budget': 4096}
        }
    )
    return response.text
