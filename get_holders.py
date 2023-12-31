# 3rd party imports
from dotenv import load_dotenv

# built-in imports
import requests, os, sys, time

# local imports


load_dotenv()

# input twitter username
username = "cobie"
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

if response.status_code == 200:
    data = response.json()
    users = data.get("users", [])
    for user in users:
        if user.get("twitterUsername") == params["username"]:
            print(user)
            address = user.get("address")
            if address:
                print("User Address:", address)
            else:
                print("User address not found.")
else:
    print("Can't get address. Error:", response.status_code)


# get holder count
if address:
    url = f"https://prod-api.kosetto.com/users/{address}/"
    response = requests.get(url, headers=None)
    group_info = response.json()

    print("Holder count", group_info["holderCount"])
#
# count = 1
#
# # get holder address list
# if address:
#
#     url = f"https://prod-api.kosetto.com/users/{address}/token/holders?"
#     response = requests.get(url, headers=None)
#     data = response.json()
#
#     for i,v in enumerate(data["users"]):
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
#         for i,v in enumerate(data["users"]):
#             print(f"{count} - {v['address']}")
#             count += 1