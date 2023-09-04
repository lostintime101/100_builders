from web3 import Web3
from dotenv import load_dotenv

load_dotenv()


rpc_list = [
    "https://1rpc.io/base",
    "https://base.meowrpc.com",
    "https://base.rpc.thirdweb.com"
]
chain_id = 8453
block_explorer = "https://basescan.org/"
# docs link: https://docs.base.org/


def create_wallet_address():
    w3 = Web3()
    new_account = w3.eth.account.create()
    print(f'New account={new_account.address}, pk={w3.to_hex(new_account.key)}')

    # TODO: pk storage
    return new_account.address
