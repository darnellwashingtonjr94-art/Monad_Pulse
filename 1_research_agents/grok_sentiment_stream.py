import os
import requests

def fetch_grok_sentiment(query: str):
    api_key = os.getenv("GROK_API_KEY")
    url = "https://api.x.ai/v1/chat/completions" # Standard xAI endpoint structure
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "grok-beta",
        "messages": [
            {"role": "system", "content": "Analyze recent market chatter and return sentiment score between -1.0 and 1.0."},
            {"role": "user", "content": f"Analyze market sentiment for: {query}"}
        ]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    return None
