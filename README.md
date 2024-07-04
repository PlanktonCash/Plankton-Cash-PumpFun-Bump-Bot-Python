# Solana Pump Transaction Script

This script sends a pump transaction to the Solana network repeatedly at a specified interval. The script is a Python adaptation of an original JavaScript implementation.

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - `solana`
  - `requests`
  - `asyncio`

## Installation

1. Clone the repository or download the script.

2. Install the required packages using pip:

   ```sh
   pip install solana requests asyncio
   ```

3. Replace the placeholder constants in the script with your actual values:
   - `RPC_URL`
   - `PRIVATE_KEY`
   - `PUBLIC_KEY`
   - `TOKEN_ADDRESS`

## Configuration

Update the following constants in the script:

- `RPC_URL`: The RPC URL of your Solana node.
- `PRIVATE_KEY`: Your wallet's private key, encoded in base58.
- `PUBLIC_KEY`: Your wallet's public key.
- `TOKEN_ADDRESS`: The token address from pump.fun.

Example:

```python
RPC_URL = "https://api.mainnet-beta.solana.com"
PRIVATE_KEY = "your_private_key"
PUBLIC_KEY = "your_public_key"
TOKEN_ADDRESS = "your_token_address"
```

## Usage

Run the script with Python:

    python pump_bot.py

The script will continuously send pump transactions at a 2-second interval.

## How It Works

    The script sends a POST request to http://api.plankton.cash with the required parameters:
        'mint': The token address.
        'publicKey': Your wallet's public key.
        'amountInSol': The amount of SOL to pump (0.01 SOL).
        'slippagePercent': Allowed slippage percentage (25%).
        'priorityFee': The priority fee (0.00001 SOL).

    If the request is successful, it receives the transaction data, signs it with your private key, and sends it to the Solana network.

    The transaction signature is printed with a link to view it on Solscan.

    The process repeats every 2 seconds.

## Adjustments

If you want to make a shorter/longer period between transactions, you can change the waiting time in :

    time.sleep(2)  # sleep for 2 seconds

by simple changing '2' to any time you want (in seconds equivalent).

## Contact

If you want to collaborate with plankton.cash platform or have any questions, please do not hesitate to contact us!

Happy bumping!
