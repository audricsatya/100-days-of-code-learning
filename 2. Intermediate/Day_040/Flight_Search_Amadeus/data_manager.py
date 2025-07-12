import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path="Intermediate/Day_040/.env")

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3cb5d478ce406a3726ba20311a156646/flightDeals/"


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_TOKEN"]
        self.header_sheety = {
            'Authorization': "Bearer " + self._user
        }
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT+'prices', headers=self.header_sheety)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    def get_user_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT+'users', headers=self.header_sheety)
        data = response.json()
        self.user_data = data["users"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.user_data
    
    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self.header_sheety,
                json=new_data
            )
            print(response.text)
