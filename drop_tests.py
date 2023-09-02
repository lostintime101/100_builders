from drop import Airdrop


newAirdrop = Airdrop()
print("activating new airdrop")
newAirdrop.activate_airdrop("0x123", ["0x123", "0x456"], 100, 100, "Hello World")
print("Status: ", newAirdrop.check_status())


print("Is Ox123 whitelisted: ", newAirdrop.is_address_whitelisted("0x123"))
print("Is Ox123 claimable: ", newAirdrop.is_address_claimable("0x123"))
print("Has Ox123 claimed: ", newAirdrop.has_address_claimed("0x123"))
print("Is time up: ", newAirdrop.is_time_up())
print("Time remaining: ", newAirdrop.check_time_remaining())

print("dropping tokens to address 0x123")
newAirdrop.drop_to_address("0x123")
print("Status: ", newAirdrop.check_status())

print("Has Ox123 claimed: ", newAirdrop.has_address_claimed("0x123"))

print("Token amount left: ", newAirdrop.check_airdrop_amount_left())
print("Claimant addresses: ", newAirdrop.get_list_of_claimed_addresses())
print("Claimant addresses and amounts: ", newAirdrop.get_claimed_addresses_and_amounts())

print("deactivating airdrop")
newAirdrop.deactivate_airdrop()
print("Status: ", newAirdrop.check_status())


