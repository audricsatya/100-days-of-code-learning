from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
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
del header, payload

access_token = token_request.json()['access_token']

datamart = DataManager(SHEETY_TOKEN)
dataflight = FlightData(access_token)
datasearch = FlightSearch(access_token)
notification = NotificationManager(USER_EMAIL, PASSWORD)

destination_data = datamart.get_data()

user_location = input("What city will you depart from? ")
TARGET_MAIL = input("Email for notification: ")

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
del data_dict, data, 

for idx, row in destination_data.iterrows():
    destination_iata = row['iataCode']
    data_flight, flight_details = datasearch.flight_list(
        user_iata=user_iata,
        destination_iata=destination_iata,
        # max_price=250,
        nonStop="false"
    )

    if data_flight.empty:
        continue

    data_flight = data_flight.sort_values("price")
    lowest = data_flight.iloc[0]

    if row['lowestPrice'] >= lowest['price']:
        message = notification.create_message(
            destination=f"{user_location} - {row['city']}",
            departure_airport=lowest['departure'],
            arrival_airport=lowest['arrival'],
            price=lowest['price']
        )

        print(message)
        notification.send_email(message, TARGET_MAIL)

        flight_details.to_excel(f"{user_location} - {row['city']}_detail.xlsx", index=False)