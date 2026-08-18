import os
from google import genai

def synthesize_macro_sentiment(news_payload: str) -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=f"Synthesize qualitative market news into a structural sentiment vector: {news_payload}",
        config={'thinking_config': {'thinking_budget': 4096}}
    )
    return response.text
