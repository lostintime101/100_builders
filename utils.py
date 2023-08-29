import re


def get_username_input():

    while True:
        username = input("Twitter username: ")
        cleaned_username = username.strip().lstrip("@")

        if re.match("^[a-zA-Z0-9_]{1,15}$", cleaned_username):
            print("Cleaned username:", cleaned_username)
            return cleaned_username

        else:
            print("Invalid username. Please provide a valid Twitter username.")