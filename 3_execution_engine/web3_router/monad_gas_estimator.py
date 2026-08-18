from web3 import Web3

def estimate_tip_transaction_gas(w3: Web3, sender: str, contract_func, value_wei: int):
    gas_estimate = contract_func.estimate_gas({
        'from': sender,
        'value': value_wei
    })
    # Apply 20% safety buffer for Monad EVM fast execution
    return int(gas_estimate * 1.20)
