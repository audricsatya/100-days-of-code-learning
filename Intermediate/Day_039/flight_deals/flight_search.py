import requests
import datetime as dt
import pandas as pd

URL = "https://test.api.amadeus.com/v2/"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token):
        self.header = {
            'accept': 'application/vnd.amadeus+json',
            'Authorization': f'Bearer {token}'
        }
    
    def flight_list(self, user_iata, destination_iata, max_depature_date = None, nonStop = "false" ,travel_class = None, currency_code = "USD", number_of_passenger = 1,  max_price = None):
        if max_depature_date is None:
            max_depature_date = (dt.datetime.now() + dt.timedelta(days=14)).strftime("%Y-%m-%d")

        parameter = {
            'originLocationCode': user_iata,
            'destinationLocationCode': destination_iata,
            'departureDate': max_depature_date,
            'adults': number_of_passenger,
            'nonStop': nonStop,
            'currencyCode': currency_code,
            'max': 250
        }

        if max_price is not None:
            parameter['maxPrice'] = max_price
        if travel_class is not None:
            if travel_class in ["ECONOMY", "PREMIUM_ECONOMY", "BUSINESS", "FIRST"]:
                parameter['travelClass'] = travel_class
            else:
                print('Travel Class wrong input. Shows every class available.')

        self.request = requests.get(URL+'shopping/flight-offers', headers=self.header, params=parameter)
        self.request.raise_for_status

        flight_json = self.request.json()
        flight_data = []

        flight_details = pd.json_normalize(flight_json['data'])

        for data in flight_json['data']:
            number_of_transit = len(data['itineraries'][0]['segments'])
            temp_data = {
                "id": data['id'],
                "source": data['source'],
                "lastTicketingDate": data['lastTicketingDate'],
                "numberOfBookableSeats": data['numberOfBookableSeats'],
                "numberOfTransit": number_of_transit,
                "totalFlightDuration": data['itineraries'][0]['duration'],
                "departure": data['itineraries'][0]['segments'][0]['departure']['iataCode'],
                "arrival": data['itineraries'][0]['segments'][number_of_transit-1]['arrival']['iataCode'],
                "currency": data['price']['currency'],
                "price": float(data['price']['grandTotal']),
                "airlines": data['validatingAirlineCodes']
            }

            flight_data.append(temp_data)

        flight_data = pd.DataFrame(flight_data)
        return flight_data, flight_details
