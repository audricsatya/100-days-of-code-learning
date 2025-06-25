import requests

BASE_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities?"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, token):
        self.header = {
            'accept': 'application/vnd.amadeus+json',
            'Authorization': f'Bearer {token}'
        }

    def get_iata_code(self, city_name) -> str:
        city_parameter = {
            "keyword": city_name,
            # "include": "AIRPORTS"
        }
        
        request = requests.get(BASE_URL, headers=self.header, params=city_parameter)
        request.raise_for_status()

        iata_code = request.json()['data'][0]['iataCode']

        print(f"iata code for city {city_name} is {iata_code}")

        return iata_code
    
