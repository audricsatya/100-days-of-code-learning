import requests
import datetime as dt
import re

API_KEY = "b198f9d1b356f652fede5bc9d60a8256" 
APP_ID = "964a9c74"
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"

WEIGHT = 82
HEIGHT = 180
AGE = 25

SHEETY_URL = 'https://api.sheety.co/3cb5d478ce406a3726ba20311a156646/workoutTracking/users'

sheet_request = requests.get(SHEETY_URL)
sheet_request_json = sheet_request.json()

user_message = input("Tell me which exercises you did?\nExample: Running for 3km and Swim 1 hour, or just running 30 minutes\n")



DATE = get_valid_date()
TIME = get_valid_time()

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    # 'x-remote-user-id': 0
}
params = {
    'query': user_message,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

nutritionix_request = requests.post(HOST_DOMAIN+END_POINT, headers=header, json=params)
data_nutritionix_json = nutritionix_request.json()

for data_exercise in data_nutritionix_json['exercises']:
    new_data = {'workout':
                {
            'date':DATE,
            'time':TIME,
            'exercise': data_exercise['name'].title(),
            'duration': data_exercise['duration_min'],
            'calories': data_exercise['nf_calories']
        }
    }
    print(new_data)

    request = requests.post(SHEETY_URL, json=new_data)
    request.raise_for_status()

request = requests.get(SHEETY_URL)
request.json()