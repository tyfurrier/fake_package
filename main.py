import getpass
import sys

import requests
from requests.auth import HTTPBasicAuth

print("Good job, you got it")


username: str = input("Please enter your atscale username registered for AtScale Connect: ")
password: str = getpass.getpass(f"Please enter the password for {username}: ")

url = ''
response = requests.get(url, auth=HTTPBasicAuth(username, password))
print(response.status_code)
print(response.ok)