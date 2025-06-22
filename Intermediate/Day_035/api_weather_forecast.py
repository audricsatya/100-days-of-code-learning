import requests
from twilio.rest import Client

# Exercise: Use the OpenWeatherMap API to get the current weather for a given city.

# Jakarta's Latitude and Longitude
LAT = -6.175110
LONG = 106.865036
ACCOUNT_SID = 'ACCOUNT_SID'  # Replace with your Twilio Account SID
AUTH_TOKEN = 'AUTH_TOKEN'  # Replace with your Twilio Auth Token
API_KEY = "API"  # Replace with your OpenWeatherMap API key
URL = "https://api.openweathermap.org/data/2.5/"
SENDER_PHONE_NUMBER = "+1234567890"  # Replace with your Twilio phone number
TARGET_PHONE_NUMBER = "+0987654321"  # Replace with your phone number

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def get_weather(city):
    """Fetch the current weather for a given city."""
    parameters = {
        "q": city,
        "appid": API_KEY,
        # "lat": LAT,
        # "lon": LONG,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(URL+"weather", params=parameters)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    if data["cod"] == 200:
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        raise ValueError(f"Error fetching weather data: {data['message']}")

def forecast_weather(LAT, LONG, COUNT):
    """Get the weather forecast for a given city."""
    parameters = {
        "lat": LAT,
        "lon": LONG,
        "appid": API_KEY,
        "cnt": COUNT,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(URL+"forecast", params=parameters)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    if data["cod"] == "200":
        forecast = []
        for item in data["list"]:
            forecast.append({
                "date": item["dt_txt"],
                "temperature": item["main"]["temp"],
                "description": item["weather"][0]["description"],
                'condition_code': item["weather"][0]["id"],
            })
        return forecast
    else:
        raise ValueError(f"Error fetching forecast data: {data['message']}")
    
# get_weather("Jakarta, ID")
data = forecast_weather(LAT, LONG, 12)

# Print emoji if rain is expected
for item in data:
    if item['condition_code'] < 700:
        MESSAGE = f"Weather Alert! 🌧️ Rain is expected on {item['date']} with a temperature of {item['temperature']}°C and condition: {item['description']}."
        print(MESSAGE)
        message = client.messages.create(
            body=MESSAGE,
            from_=SENDER_PHONE_NUMBER,  # Replace with your Twilio phone number
            to=TARGET_PHONE_NUMBER  # Replace with your phone number,
        )
    else:
        print(f"Date: {item['date']}, Temperature: {item['temperature']}°C, Description: {item['description']}")
