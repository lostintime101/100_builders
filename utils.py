# 3rd party
from sqlalchemy import select, join
from sqlmodel import Session
from db_tables_setup import Airdrop, Whitelist, Activation

# built-in
import json, re, random
from uuid import uuid4, uuid5

# local


def get_username_input():

    while True:
        username = input("Twitter username: ")
        cleaned_username = username.strip().lstrip("@")

        if re.match("^[a-zA-Z0-9_]{1,15}$", cleaned_username):
            print("Cleaned username:", cleaned_username)
            return cleaned_username

        else:
            print("Invalid username. Please provide a valid Twitter username.")


def get_new_nonce():

    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    config_data["last_nonce"] = str(int(config_data["last_nonce"]) + 1)

    with open("config.json", "w") as config_file:
        json.dump(config_data, config_file, indent=4)

    return config_data["last_nonce"]


# calculates a random amount of tokens to send to the claimant
def generate_random_amount(airdrop_object):

    airdrop_object = airdrop_object.__dict__
    randomness = airdrop_object["randomness"]
    recipients = airdrop_object["recipients"]
    activated = airdrop_object["activated"]
    total_addresses_claimed = airdrop_object["total_addresses_claimed"]
    gas_token_amount = airdrop_object["gas_token_amount"]

    # if activated != Activation.activated:
    #     return ValueError("Airdrop is not activated")

    if total_addresses_claimed >= recipients:
        print(total_addresses_claimed, recipients)
        return ValueError("Too late! Max number of addresses already claimed")
    if gas_token_amount <= 0:
        return ValueError("Gas token amount is 0")

    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)

    low, high = config_data["randomness"][randomness]

    base_amount = round(gas_token_amount / (recipients - total_addresses_claimed), 4)
    amount = round(base_amount + (base_amount * (random.randint(low, high) / 100)), 4)

    return amount


# need this as gas calculation will be different for last claimant
def is_this_the_last_claimant():
    ...


# use the whitelist id to grab all info about the airdrop
def get_airdrop_info_by_whitelist_id(_whitelist_id, engine):

    with Session(engine) as session:

        whitelist = session.query(Whitelist).filter(Whitelist.id == _whitelist_id).first()

        if whitelist:
            # Convert the Row object to a Whitelist model instance
            db_airdrop = session.query(Airdrop).filter(Airdrop.id == whitelist.airdrop_id).first()
            # print("db_airdrop", db_airdrop)

        # TODO: add error handling

        return db_airdrop


