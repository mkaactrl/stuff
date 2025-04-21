import random
import string
import requests

def generate_word():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

def check_username(username):
    url = f"https://www.roblox.com/usersignup/usernames/available?username={username}"
    response = requests.get(url)
    
    # Debugging: Show the full response (you should see the status and the available field)
    print(f"Response: {response.text}")  # Print the raw response text
    
    # Check if response was successful
    if response.status_code == 200:
        json_response = response.json()
        # Debugging: Print the actual JSON response to see if the 'available' field exists
        print(f"JSON Response: {json_response}")
        
        if 'available' in json_response:  # Check if the 'available' key exists
            if json_response['available']:
                print(f"{username} is AVAILABLE!")
            else:
                print(f"{username} is TAKEN!")
        else:
            print(f"Error: 'available' field not found in the response for {username}")
    else:
        print(f"Error: Failed to fetch username data. Status code: {response.status_code}")

# Testing the check function
while True:
    username = generate_word()
    print(f"Checking {username}...")
    check_username(username)
