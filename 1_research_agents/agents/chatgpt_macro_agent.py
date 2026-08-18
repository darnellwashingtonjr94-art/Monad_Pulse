import os
from openai import OpenAI

def query_chatgpt_macro_regime(market_state: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Assess global macro liquidity conditions for this data: {market_state}"}]
    )
    return response.choices[0].message.content
