import os
from web3 import Web3

class MonadDEXProvider:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(os.getenv("MONAD_RPC_URL", "https://testnet-rpc.monad.xyz")))
    
    def get_latest_block_number(self):
        return self.w3.eth.block_number

    def get_gas_price(self):
        return self.w3.eth.gas_price
