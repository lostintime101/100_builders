from datetime import datetime
from typing import Dict, List, Optional

LIFETIME_SECONDS = 86_400  # 24 hours

""" managing pks will be dealt with separately """


class Airdrop:
    def __init__(self, creator: str, whitelist: List[str], recipients: int, amount: int, message: str = None):
        self.address = ""  # TODO: logic for generating fresh address
        self.created_at = datetime.now()
        self.gas_token_amount = 0  # can be same as airdrop_token_amount
        self.airdrop_token_amount = amount
        self.airdrop_token_address = ""
        self.current_token_balance = 0
        self.creator = creator
        self.message = message
        self.whitelist = {}
        self.recipients = recipients  # must be less than or equal to length of whitelist, cannot be 0 or negative
        self.total_addresses_claimed = 0
        self.activated = False
        self.activated_at = None
        for address in whitelist: self.whitelist[address] = None

    def activate_airdrop(self):

        if self.activated: return ValueError("Airdrop already active")
        self.activated = True
        self.activated_at = datetime.now()

    def deactivate_airdrop(self):
        self.activated = False
        if self.current_token_balance > 0:
            ...  # TODO: logic for returning tokens to creator

    def drop_to_address(self, claimant: str):

        if not self.activated:
            return ValueError("Airdrop not active")

        if self.is_time_up():
            self.deactivate_airdrop()
            return ValueError("Airdrop time is up")

        if self.total_addresses_claimed >= self.recipients:
            self.deactivate_airdrop()
            return ValueError("Max recipients reached")

        if self.has_address_claimed(claimant):
            return ValueError("Address already claimed")

        if not self.is_address_whitelisted(claimant):
            return ValueError("Address not on whitelist")

        if self.current_token_balance <= 0:
            self.deactivate_airdrop()
            return ValueError("Airdrop balance depleted")

        amount = 1  # TODO: logic for calculating random amount to drop

        #  TODO: logic for dropping tokens to address

        self.whitelist[claimant] = amount
        self.current_token_balance -= amount
        self.total_addresses_claimed += 1

        return amount

    def check_status(self):

        if not self.activated:
            return {
                "Status": "Inactive"
            }

        current_time = datetime.now()

        return {
            "Status": "Active",
            "Time remaining": LIFETIME_SECONDS - (current_time - self.activated_at).seconds,
            "Addresses claimed": f"{self.total_addresses_claimed} / {self.recipients}",
            "Percentage claimed": f"{(self.total_addresses_claimed / self.recipients)*100}%",
            "Current balance": self.current_token_balance
        }

    def check_time_remaining(self):

        if not self.activated:
            return ValueError("Airdrop not active")

        current_time = datetime.now()
        time_remaining = LIFETIME_SECONDS - (current_time - self.activated_at).seconds

        return time_remaining

    def is_time_up(self):
        return self.check_time_remaining() <= 0

    def check_airdrop_amount_left(self):
        return self.current_token_balance

    def get_list_of_claimed_addresses(self):
        return [k for k, v in self.whitelist.items() if v is not None]

    def get_claimed_addresses_and_amounts(self):
        return [(k, v) for k, v in self.whitelist.items() if v is not None]

    def has_address_claimed(self, address: str):
        return address in self.whitelist and self.whitelist[address] is not None

    def is_address_whitelisted(self, address: str):
        return address in self.whitelist.keys()

    def is_address_claimable(self, address: str):
        return self.is_address_whitelisted(address) and not self.has_address_claimed(address)

    def get_address_claimed_amount(self, address: str):
        return self.whitelist[address]
