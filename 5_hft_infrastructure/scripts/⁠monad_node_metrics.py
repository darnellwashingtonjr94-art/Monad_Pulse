import time
import requests

def fetch_monad_node_stats():
    url = "http://localhost:8545"
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    start = time.time()
    res = requests.post(url, json=payload).json()
    latency = (time.time() - start) * 1000
    print(f"Monad RPC Latency: {latency:.2f}ms | Current Block: {int(res['result'], 16)}")
