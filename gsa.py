import requests
import uuid
import random

# Base URL for the API endpoint
BASE_URL = "https://aiskillshouse.com/olivrweb/user/Api.php/setScore"

# Parameters from the original URL
UID = "7844"
PROMPT_ID = "17"

def generate_fake_data():
    """Generates unique deviceId and a fake IP address."""
    # Generate a unique deviceId similar to FingerprintJS output
    device_id = uuid.uuid4().hex
    
    # Generate a fake public IP address
    ip_address = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    
    return device_id, ip_address

def simulate_engagement():
    """Simulates a single successful engagement by sending a POST request."""
    device_id, ip_address = generate_fake_data()
    
    payload = {
        'uid': UID,
        'promptId': PROMPT_ID,
        'deviceId': device_id,
        'ipAddress': ip_address
    }
    
    try:
        response = requests.post(BASE_URL, data=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        data = response.json()
        
        if data.get('status') == True:
            print(f"Success! Engagement simulated for Device ID: {device_id}, IP: {ip_address}")
            print(f"Response: {data}")
            return True
        else:
            print(f"Failed! API returned status 'false'.")
            print(f"Response: {data}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# ----- Main Simulation Loop -----
if __name__ == "__main__":
    num_engagements = 2 # Number of engagements to simulate
    
    print(f"Starting simulation of {num_engagements} engagements...")
    
    for i in range(num_engagements):
        print(f"\n--- Simulating Engagement {i + 1}/{num_engagements} ---")
        simulate_engagement()