from web3 import Web3

# 1. Connect to Monad RPC Node
w3 = Web3(Web3.HTTPProvider('RPC_URL_HERE'))
private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

contract_address = w3.to_checksum_address("YOUR_DEPLOYED_CONTRACT_ADDRESS")
abi = [ ... ] # ABI from compiled contract above
contract = w3.eth.contract(address=contract_address, abi=abi)

# Example 1: Send 10 MON with 2.5% optional tip
def send_mon_with_tip(destination_address):
    tx = contract.functions.processMON(
        w3.to_checksum_address(destination_address),
        True,  # applyTip = True
        250    # tipBps = 250 (2.5%)
    ).build_transaction({
        'from': account.address,
        'value': w3.to_wei(10.0, 'ether'),
        'nonce': w3.eth.get_transaction_count(account.address),
        # Add Monad specific gas parameters here
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash
