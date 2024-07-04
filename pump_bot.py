import time
import requests
from solders.transaction import VersionedTransaction
from solders.keypair import Keypair
from solders.commitment_config import CommitmentLevel
from solders.rpc.requests import SendVersionedTransaction
from solders.rpc.config import RpcSendTransactionConfig

# Constants
RPC_URL = "YOUR_RPC_URL"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
PUBLIC_KEY = "YOUR_PUBLIC_KEY"
TOKEN_ADDRESS = "YOUR_TOKEN_ADDRESS"

def send_pump_transaction():
    response = requests.post(url="http://api.plankton.cash", data={
        "mint": TOKEN_ADDRESS,     # Token address from pump.fun
        "publicKey": PUBLIC_KEY, # Your wallet public key
        "amountInSol": 0.1,            # Amount of SOL, (0.1 SOL)
        "slippagePercent": 25,              # Percent slippage allowed (25%)
        "priorityFee": 0.00001,        # Priority fee (0.00001 SOl) - the lower priority fee, the lower chance to be taken by solana network
    })
    if response.status_code == 200:
        keypair = Keypair.from_base58_string(PRIVATE_KEY)
        tx = VersionedTransaction(VersionedTransaction.from_bytes(response.content).message, [keypair])

        commitment = CommitmentLevel.Confirmed
        config = RpcSendTransactionConfig(preflight_commitment=commitment)
        txPayload = SendVersionedTransaction(tx, config)

        response = requests.post(
            url=RPC_URL,
            headers={"Content-Type": "application/json"},
            data=SendVersionedTransaction(tx, config).to_json()
        )
        txSignature = response.json()['result']
        print(f'Transaction: https://solscan.io/tx/{txSignature}')
    else:
        print(response.json())

def main():
    while True: 
        send_pump_transaction()
        time.sleep(2)  # sleep for 2 seconds

main()