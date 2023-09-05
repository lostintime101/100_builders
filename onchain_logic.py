# 3rd party
from web3 import Web3, HTTPProvider
from eth_account import Account

# built-in
import os
from dotenv import load_dotenv

# local


# globals
BASE_CHAIN_ID = 8453
BASE_BLOCK_EXPLORER = "https://basescan.org/"
HIGH_GAS_STANDARD = 50

load_dotenv()


# creates a new address for dispatching the airdrop
def get_new_dispatcher_address(nonce):

    Account.enable_unaudited_hdwallet_features()
    new_acct = Account.from_mnemonic(os.getenv("PHRASE"), account_path=f"{os.getenv('ACCOUNT_PATH')}{nonce}")

    return new_acct.address


# gets the dispatch account object from the address
def get_dispatcher_object(nonce):

    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(os.getenv("PHRASE"), account_path=f"{os.getenv('ACCOUNT_PATH')}{nonce}")

    return account


# listen for the onchain event of the wallet being funded from the creator's wallet
def listen_for_funding(creator_address, dispatch_address):

    base = Web3(HTTPProvider(os.getenv("RPC_1")))
    # https://web3py.readthedocs.io/en/stable/filters.html
    filter_params = {
        'fromBlock': 'latest',
        'toBlock': 'latest',
        'address': dispatch_address,
        'topics': [None, Web3.to_hex(text=f"{creator_address}")]
    }

    event_filter = base.eth.filter(filter_params)
    # TODO: finish this function along with front-end


# fetch current gas prices from mainnet and base
def fetch_gas_prices():

    mainnet = Web3(HTTPProvider("https://rpc.flashbots.net/"))
    mainnet_recent_gas_raw_array = mainnet.eth.fee_history(3, mainnet.eth.block_number)["baseFeePerGas"]  # returns 3 + 1 blocks, 1 being the next block
    mainnet_recent_gas_prices = [mainnet.from_wei(value, 'gwei') for value in mainnet_recent_gas_raw_array]
    mainnet_next_block_gas_gwei = mainnet_recent_gas_prices[-1]

    base = Web3(HTTPProvider(os.getenv("RPC_1")))
    base_recent_gas_raw_array = base.eth.fee_history(3, base.eth.block_number)["baseFeePerGas"]  # returns 3 + 1 blocks, 1 being the next block
    base_recent_gas_prices = [base.from_wei(value, 'gwei') for value in base_recent_gas_raw_array]
    base_next_block_gas_gwei = base_recent_gas_prices[-1]
    base_next_block_gas_wei = base.to_wei(base_next_block_gas_gwei, 'gwei')

    return {
        "mainnet_next_block_gas_gwei": mainnet_next_block_gas_gwei,
        "base_next_block_gas_gwei": base_next_block_gas_gwei,
        "base_next_block_gas_wei": base_next_block_gas_wei
        }


# fetch current eth balance of dispatch address
def fetch_eth_balance(dispatch_address):
    base = Web3(HTTPProvider(os.getenv("RPC_1")))
    current_eth = base.eth.get_balance(dispatch_address)
    return current_eth


# send randomized amount to whitelisted address
def make_transaction(nonce, recipient_address, amount):

    base = Web3(HTTPProvider(os.getenv("RPC_1")))
    dispatcher = get_dispatcher_object(nonce)

    gas = fetch_gas_prices()
    mainnet_gas_gwei, base_gas_gwei, base_gas_wei = gas["mainnet_next_block_gas_gwei"], gas["base_next_block_gas_gwei"], gas["base_next_block_gas_wei"]

    max_priority_fee_per_gas = base.eth.max_priority_fee
    max_priority_fee_per_gas = min(base_gas_wei, max_priority_fee_per_gas)

    max_fee_per_gas = base_gas_wei + int(base_gas_wei * 0.1)  # NOT SURE IF THIS IS NEEDED

    transaction = {
        "chainId": BASE_CHAIN_ID,
        "from": base.to_checksum_address(dispatcher.address),
        "nonce": base.eth.get_transaction_count(base.to_checksum_address(dispatcher.address)),
        "maxFeePerGas": max_fee_per_gas,
        "maxPriorityFeePerGas": max_priority_fee_per_gas,
        "to": base.to_checksum_address(recipient_address),
        "value": amount,
        "gas": 21_000 # TODO: double check this is correct for base
    }

    signed = base.eth.account.sign_transaction(transaction, dispatcher.key)
    tx_hash = base.eth.send_raw_transaction(signed.rawTransaction)

    print("Transaction hash: ", Web3.to_hex(tx_hash))

    link = f"{BASE_BLOCK_EXPLORER}/tx/{Web3.to_hex(tx_hash)}"
    print(f"\033[4;34;47mBlock Explorer: \033[0m\033]8;;{link}\033\\{link}\033]8;;\033\\")

    print("Waiting for receipt...")
    receipt = base.eth.wait_for_transaction_receipt(Web3.to_hex(tx_hash))
    print(receipt)

    return receipt


