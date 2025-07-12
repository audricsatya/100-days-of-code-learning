import requests
import pandas as pd

SHEETY_URL = "https://api.sheety.co/3cb5d478ce406a3726ba20311a156646/flightDeals/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_token):
        self.header_sheety = {
            'Authorization': "Bearer " + sheety_token
        }

    def get_data(self,sheet='prices'):
        self.data_prices_json = requests.get(SHEETY_URL+sheet, headers=self.header_sheety).json()
        data_prices = pd.DataFrame(self.data_prices_json[sheet])
        return data_prices

    def edit_data(self, json_file, object_id, sheet='prices'):
        try:
            requests.put(f'{SHEETY_URL}{sheet}/{object_id}', headers=self.header_sheety, json=json_file)
            print(f"id {object_id}: Successfully updated")
        except Exception as e:
            print(f"id {object_id}: error")
            print(e)
