import os
import sys

def audit_environment():
    required_vars = ["MONAD_RPC_URL", "PRIVATE_KEY", "ROUTER_CONTRACT_ADDRESS", "GROK_API_KEY", "GEMINI_API_KEY"]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        print(f"CRITICAL: Missing required environment keys: {missing}")
        sys.exit(1)
    print("System Environment Audit Passed: All variables present.")

if __name__ == "__main__":
    audit_environment()
