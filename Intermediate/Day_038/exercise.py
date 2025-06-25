from dotenv import load_dotenv
import os

from Intermediate.Day_038.sheety import WorkOutSheet

load_dotenv(dotenv_path="Intermediate/Day_038/.env")

API_KEY = os.getenv("NUTRITIONIX_API_KEY")
APP_ID = os.getenv("NUTRITIONIX_APP_ID")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"
sheety = WorkOutSheet(SHEETY_TOKEN,API_KEY,APP_ID)

sheety.is_login()
while True:
    while True:
        choice = input("What do you want to do?\n1. Add Workout\n2. Edit Profile\n3. Get Workout Data\n0. Exit\n\nInput number only: ")
        try:
            choice = int(choice)
            if choice in [0, 1, 2, 3]:
                break
            else:
                print("Please enter the number")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, 2 or 3).")

    if choice == 1:
        user_message = input("Tell me which exercises you did?\nExample: Running for 3km and Swim 1 hour, or just running 30 minutes\n")
        sheety.add_workout(user_message)
    elif choice == 2:
        edit_choice = input("What do you want to edit? (height/weight/age/all): ").strip().lower()
        if edit_choice == "all":
            new_height = input("Enter new height: ")
            new_weight = input("Enter new weight: ")
            new_age = input("Enter new age: ")
            sheety.edit_user(height=new_height, weight=new_weight, age=new_age)
        elif edit_choice in ["height", "weight", "age"]:
            new_value = input(f"Enter new {edit_choice}: ")
            if edit_choice == "height":
                sheety.edit_user(height=new_value)
            elif edit_choice == "weight":
                sheety.edit_user(weight=new_value)
            elif edit_choice == "age":
                sheety.edit_user(age=new_value)
        else:
            print("Invalid choice. Please enter 'height', 'weight', 'age', or 'all'.")
    elif choice == 3:
        sheety.get_workout_data()
    else:
        print("Thank you for using the app")
        break