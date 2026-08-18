from web3 import Web3

def listen_to_router_events(w3: Web3, contract_address, abi):
    contract = w3.eth.contract(address=contract_address, abi=abi)
    event_filter = contract.events.NativeTransferWithTip.create_filter(from_block='latest')
    print("Listening for Monad router tip and transaction events...")
    return event_filter
