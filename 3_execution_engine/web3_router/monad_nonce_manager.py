from web3 import Web3

class MonadNonceManager:
    def __init__(self, w3: Web3, address: str):
        self.w3 = w3
        self.address = w3.to_checksum_address(address)
        self.current_nonce = w3.eth.get_transaction_count(self.address, 'pending')

    def get_next_nonce(self):
        nonce = self.current_nonce
        self.current_nonce += 1
        return nonce
