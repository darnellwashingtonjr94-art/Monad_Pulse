import os
import websocket

def on_message(ws, message):
    print(f"Grok Live Stream Packet: {message}")

def start_grok_websocket():
    ws_url = "wss://api.x.ai/v1/stream" # Example streaming socket
    ws = websocket.WebSocketApp(ws_url, on_message=on_message)
    ws.run_forever()
