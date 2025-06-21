# This code is for educational purposes only. Use responsibly and ethically.
import requests

# ISS Location API
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # Raise an error for bad responses

if response.status_code == 200:
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    print(f"Current ISS Location: Latitude {latitude}, Longitude {longitude}")