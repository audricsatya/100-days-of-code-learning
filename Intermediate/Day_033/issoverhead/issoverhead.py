# This code is for educational purposes only. Use responsibly and ethically.
# This code checks if the International Space Station (ISS) is currently overhead and if it is dark at the user's location (Jakarta, Indonesia).

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password"

# Jakarta's Latitude and Longitude
MY_LAT = -6.175110 
MY_LONG = 106.865036 
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

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    local_sunrise = utc_to_local(sunrise)
    local_sunset = utc_to_local(sunset)

    time_now = datetime.now()
    if local_sunrise >= time_now.hour or local_sunset <= time_now.hour:
        return True

#If the ISS is close to my current position and it is currently dark
while True:
    if is_iss_overhead() and is_dark():
        # Send an email notification
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is overhead and it's dark outside!"
            )
        break
    time.sleep(60)  # Wait for 60 seconds before checking again 