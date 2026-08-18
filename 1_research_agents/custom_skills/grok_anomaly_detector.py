import os
import requests

def check_grok_volume_anomaly(keyword: str):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {os.getenv('GROK_API_KEY')}", "Content-Type": "application/json"}
    payload = {
        "model": "grok-beta",
        "messages": [{"role": "user", "content": f"Is there an abnormal social volume spike for {keyword} right now? Answer TRUE or FALSE."}]
    }
    res = requests.post(url, json=payload, headers=headers)
    return res.json()['choices'][0]['message']['content']
