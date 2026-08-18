import os
import json

def generate_report():
    report = {
        "env_vars_set": [k for k in ["MONAD_RPC_URL", "PRIVATE_KEY", "ROUTER_CONTRACT_ADDRESS"] if os.getenv(k)],
        "workspace_status": "READY"
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    generate_report()
