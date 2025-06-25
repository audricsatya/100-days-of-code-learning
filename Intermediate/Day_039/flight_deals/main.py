from Intermediate.Day_039.flight_deals.data_manager import DataManager
from Intermediate.Day_039.flight_deals.flight_data import FlightData
from Intermediate.Day_039.flight_deals.flight_search import FlightSearch
from Intermediate.Day_039.flight_deals.notification_manager import NotificationManager
from dotenv import load_dotenv

import os
import requests
import pandas as pd

load_dotenv(dotenv_path="Intermediate/Day_039/.env")

SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")
USER_EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASS")

URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
header = {
    "Content-Type": "application/x-www-form-urlencoded"
}
payload = {
    "grant_type" : "client_credentials",
    "client_id" : AMADEUS_KEY,
    "client_secret": AMADEUS_SECRET
}

token_request = requests.post(URL, headers=header, data=payload)
access_token = token_request.json()['access_token']

datamart = DataManager(SHEETY_TOKEN)
dataflight = FlightData(access_token)
datasearch = FlightSearch(access_token)
notification = NotificationManager(USER_EMAIL, PASSWORD)

destination_data = datamart.get_data()

user_location = input("What city will you depart from? ")

user_iata = dataflight.get_iata_code(user_location)

# Data Checker simulation
data_dict = datamart.data_prices_json['prices']

for data in data_dict:
    if data['iataCode'] == "":
        iata_code = dataflight.get_iata_code(data['city'])
        data['iataCode'] = iata_code
        updated_json = {
            'price':data
        }
        datamart.edit_data(updated_json, data['id'])
del data_dict, data

data_flight, flight_details = datasearch.flight_list(
    user_iata=user_iata, 
    destination_iata="SIN", 
    max_depature_date="2025-07-30", 
    max_price=250,
    nonStop="false"
)
pd.json_normalize(datasearch.request.json()['data'])

data_flight.sort_values(["price"])
data_flight['price'] = data_flight['price'].astype(float)

lowest = data_flight.loc[data_flight['price'].idxmin()]

