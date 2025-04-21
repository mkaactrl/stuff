import random
import string
import requests
from bs4 import BeautifulSoup

def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

def check_username(username):
    url = f"https://www.roblox.com/usersignup/usernames/available?username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        if json_response['available']:
            print(f"{username} is AVAILABLE!")
        else:
            print(f"{username} is TAKEN!")
    else:
        print("Error checking username.")

while True:
    username = generate_word()
    print(f"Checking {username}...")
    check_username(username)
