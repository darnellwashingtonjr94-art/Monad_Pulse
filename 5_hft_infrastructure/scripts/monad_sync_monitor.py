import time
from web3 import Web3

def monitor_sync_status(w3: Web3):
    while True:
        is_syncing = w3.eth.syncing
        if not is_syncing:
            print("Monad Node is fully synchronized.")
            break
        print(f"Syncing... Current block: {is_syncing.get('currentBlock', 0)}")
        time.sleep(2)
