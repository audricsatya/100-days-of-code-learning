# This code is for educational purposes only. Use responsibly and ethically.
import requests
import datetime as dt

# Jakarta's Latitude and Longitude
MY_LATITUDE = -6.175110
MY_LONGITUDE = 106.865036

url = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": MY_LATITUDE, 
    "lng": MY_LONGITUDE, 
    "formatted": 0
}

LOCAL_UTC_OFFSET = 7  # Jakarta is UTC+7
# Function to convert UTC hour to local time
 
def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

response = requests.get(url=url, params=parameters)
response.raise_for_status()  # Raise an error for bad responses
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
local_sunrise = utc_to_local(sunrise)
local_sunset = utc_to_local(sunset)

time_now = dt.datetime.now()

print(f"Local Sunrise: {local_sunrise}")
print(f"Local Sunset: {local_sunset}")
print(f"Current Time: {time_now.hour}")