from web3 import Web3

def bundle_and_sign_transactions(w3: Web3, private_key, tx_list):
    """Bundles multiple transaction payloads for rapid Monad EVM submission."""
    signed_txs = []
    for tx in tx_list:
        signed = w3.eth.account.sign_transaction(tx, private_key)
        signed_txs.append(signed.rawTransaction)
    return signed_txs
