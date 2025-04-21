import random
import string
import requests

# Define log file
log_file = "debug_log.txt"

def log_message(message):
    with open(log_file, "a") as file:
        file.write(message + "\n")
    print(message)

def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

def check_username(username):
    url = f"https://www.roblox.com/usersignup/usernames/available?username={username}"
    response = requests.get(url)
    
    # Log and print the raw response for debugging
    log_message(f"Response for {username}: {response.text}")
    
    if response.status_code == 200:
        try:
            json_response = response.json()
            log_message(f"JSON Response for {username}: {json_response}")
            
            if 'available' in json_response:
                if json_response['available']:
                    log_message(f"{username} is AVAILABLE!")
                else:
                    log_message(f"{username} is TAKEN!")
            else:
                log_message(f"Error: 'available' field not found in the response for {username}")
        except ValueError:
            log_message(f"Error: Could not parse JSON for {username}")
    else:
        log_message(f"Error: Failed to fetch username data for {username}. Status code: {response.status_code}")

# Testing the check function
while True:
    username = generate_word()
    log_message(f"Checking {username}...")
    check_username(username)
