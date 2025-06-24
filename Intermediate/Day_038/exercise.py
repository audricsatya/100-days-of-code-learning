import requests
import datetime as dt
from dotenv import load_dotenv
import os

from sheety import WorkOutSheet

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("NUTRITIONIX_API_KEY")
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"

sheety = WorkOutSheet()



sheety.is_login()
while True:
    while True:
        choice = input("What do you want to do?\n1. Add Workout\n2. Edit Profile\n0. Exit\n\nInput number only: ")
        try:
            choice = int(choice)
            if choice in [0, 1, 2]:
                break
            else:
                print("Please enter the number")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

    if choice == 1:
        user_message = input("Tell me which exercises you did?\nExample: Running for 3km and Swim 1 hour, or just running 30 minutes\n")
        sheety.add_workout(user_message)
    elif choice == 2:
        sheety.get_workout_data()
    else:
        print("Thank you for using the app")
        break