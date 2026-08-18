import os
import sys

def check_env():
    keys = ["MONAD_RPC_URL", "PRIVATE_KEY", "ROUTER_CONTRACT_ADDRESS"]
    for k in keys:
        if not os.getenv(k):
            print(f"Error: Environment variable {k} is missing.")
            sys.exit(1)
    print("All core environment keys verified.")

if __name__ == "__main__":
    check_env()
