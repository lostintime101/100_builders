from datetime import datetime
from typing import Dict, List

LIFETIME_SECONDS = 86_400  # 24 hours


class Airdrop:
    def __init__(self):
        self.address = ""  # TODO: logic for generating fresh address
        self.pk = ""
        self.created_at = datetime.now()
        self.gas_token = 0
        self.airdrop_token_amount = 0
        self.airdrop_token_address = ""
        self.current_balance = 0
        self.creator = None
        self.message = None
        self.whitelist = {}
        self.claimed = {}
        self.recipients = 0
        self.total_addresses_claimed = 0
        self.activated = False
        self.activated_at = None

    def activate_airdrop(self, creator: str, whitelist: List[str], recipients: int, amount: int, message: str = None):

        if self.activated:
            return ValueError("Airdrop already active")

        self.activated = True
        self.creator = creator
        self.airdrop_token_amount = amount
        self.current_balance = amount
        self.message = message
        self.recipients = recipients
        self.activated_at = datetime.now()
        for address in whitelist: self.whitelist[address] = True

    def deactivate_airdrop(self):
        self.activated = False
        if self.current_balance > 0:
            ...  # TODO: logic for returning tokens to creator

    def drop_to_address(self, claimant: str):

        if not self.activated:
            return ValueError("Airdrop not active")

        if self.is_time_up():
            self.deactivate_airdrop()
            return ValueError("Airdrop time is up")

        if self.total_addresses_claimed >= self.recipients:
            self.deactivate_airdrop()
            return ValueError("All addresses claimed")

        if self.has_address_claimed(claimant):
            self.deactivate_airdrop()
            return ValueError("Address already claimed")

        if not self.is_address_whitelisted(claimant):
            self.deactivate_airdrop()
            return ValueError("Address not on whitelist")

        if self.current_balance <= 0:
            self.deactivate_airdrop()
            return ValueError("Airdrop balance depleted")

        amount = 1  # TODO: logic for calculating random amount to drop

        #  TODO: logic for dropping tokens to address

        self.claimed[claimant] = amount
        self.whitelist[claimant] = False
        self.current_balance -= amount
        self.total_addresses_claimed = len(self.claimed)

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
            "Current balance": self.current_balance
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
        return self.current_balance

    def get_list_of_claimed_addresses(self):
        return self.claimed.keys()

    def get_claimed_addresses_and_amounts(self):
        return self.claimed.items()

    def has_address_claimed(self, address: str):
        return address in self.claimed

    def is_address_whitelisted(self, address: str):
        return address in self.whitelist

    def is_address_claimable(self, address: str):
        return self.is_address_whitelisted(address) and not self.has_address_claimed(address)

    def get_address_claimed_amount(self, address: str):
        return self.claimed[address]
