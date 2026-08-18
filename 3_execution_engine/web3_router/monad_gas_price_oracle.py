from web3 import Web3

def get_optimal_monad_gas_price(w3: Web3):
    base_fee = w3.eth.gas_price
    # Add 10% priority adjustment for high-frequency inclusion
    optimized_gas = int(base_fee * 1.10)
    return optimized_gas
