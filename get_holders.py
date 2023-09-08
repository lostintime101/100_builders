# 3rd party imports
from dotenv import load_dotenv

# built-in imports
import requests, os, sys, time, re


"""

This script will take the address of a twitter user and then grab the holder count 
and list of holder addresses for that user on Friend Tech.

Addresses are paginated, so this script will grab the first page of addresses, 
then check if there is a next page, and if so, grab that page, and so on until there are no more pages.

Address list includes only holders with a valid Friend Tech account.
So for example a bot snipping keys directly from the contract without an account is technically a holder but not be included in the list.

"""

load_dotenv()



async def fetch_key_holders(username: str):

    cleaned_username = username.strip().lstrip("@")

    if re.match("^[a-zA-Z0-9_]{1,15}$", cleaned_username):
        print("Cleaned username:", cleaned_username)
    else:
        raise ValueError("Invalid username. Please provide a valid Twitter username.")

    return cleaned_username

    address = None

    # get address
    url = "https://prod-api.kosetto.com/search/users"
    headers = {
        "Authorization": os.getenv("JWT"),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Referer": "https://www.friend.tech/"
    }

    params = {
        "username": username
    }

    response = requests.get(url, headers=headers, params=params)
    user = None

    if response.status_code == 200:
        data = response.json()
        users = data.get("users", [])
        for user in users:
            if user.get("twitterUsername") == params["username"]:
                address = user.get("address")
                if address:
                    print("User Address:", address)
                else:
                    raise ValueError("Twitter user not found.")
                break
    else:
        raise ValueError("Can't get address. Error:", response.status_code)

    if user: return user
    else: raise ValueError("Twitter user not found.")


# get holder count
# if address:
#     url = f"https://prod-api.kosetto.com/users/{address}/"
#     response = requests.get(url, headers=None)
#     group_info = response.json()
#
#     print("Holder count", group_info["holderCount"])
#
# count = 1


# get holder address list
# if address:
#
#     url = f"https://prod-api.kosetto.com/users/{address}/token/holders?"
#     response = requests.get(url, headers=None)
#     data = response.json()
#
#     for i, v in enumerate(data["users"]):
#         print(f"{count} - {v['address']}")
#         count += 1
#
#     while data["nextPageStart"]:
#
#         time.sleep(3)
#         url = f"https://prod-api.kosetto.com/users/{address}/token/holders?pageStart={data['nextPageStart']}"
#         response = requests.get(url, headers=None)
#         data = response.json()
#
#         for i, v in enumerate(data["users"]):
#             print(f"{count} - {v['address']}")
#             count += 1
