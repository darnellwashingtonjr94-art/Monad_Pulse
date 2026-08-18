import os
from google import genai

def audit_execution_logs(log_data: str) -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=f"Analyze these trade execution logs for slippage anomalies and latency bottlenecks: {log_data}",
        config={'thinking_config': {'thinking_budget': 4096}}
    )
    return response.text
