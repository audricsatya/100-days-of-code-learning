import requests
import pandas as pd
import os

SHEETY_URL = 'https://api.sheety.co/3cb5d478ce406a3726ba20311a156646/workoutTracking/'
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"

class WorkOutSheet:
    def __init__(self, sheety_token, nutritionix_token, nutritionix_app_id):
        self.workout_data = requests.get(SHEETY_URL+"workouts").json()
        self.user_data = requests.get(SHEETY_URL+"users").json()
        self.user_list = pd.DataFrame(self.user_data['users'])['username'].to_list()
        self.username = None
        self.header_sheety = {
            'Authorization': "Bearer " + sheety_token
        }
        self.header_nutritionix = {
            'x-app-id': nutritionix_app_id,
             'x-app-key': nutritionix_token,
        }

    def is_login(self):
        is_login = True
        while is_login is True:
            is_registered = input("Welcome to workout tracker. Do you already have an account?(Y/N) ")
            if is_registered.upper() == "Y":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.get_user(username, password)
            elif is_registered.upper() == "N":
                self.create_user()
                print("Account created. Please login again.")
            else:
                print("Let's try again. Input only Y or N\n")
                os.system('cls' if os.name == 'nt' else 'clear')

    def check_username(self,username):
        while True:
            if username in self.user_list:
                username = input("username already taken.\nEnter other username: ")
            else:
                print("username available")
                return username

    def create_user(self):
        username = input("Enter your username: ")
        username = self.check_username(username)
        name = input("Enter your name: ")
        height = input("Enter your height: ")
        weight = input("Enter your weight: ")
        age = input("Enter your age: ")
        password = input("Enter your password:\n(Do Not Forget. Contact Admin if you are.)\n")
        new_user= {
            'user':{
                'username': username,
                'name': name.title(),
                'height': height,
                'weight': weight,
                'age': age,
                'password': password
            }
        }
        requests.post(SHEETY_URL+"users", headers=self.header_sheety, json=new_user)

    def get_user(self, username, password):
        while True:
            for user in self.user_data['users']:
                if user['username'] == username and user['password'] == password:
                    print("Login successful.")
                    self.username == username
                    return user
            choice = input("Invalid credentials. Try again or type 'create new account': ").strip().lower()
            if choice == "create new account":
                self.create_user()
                print("Account created. Please login again.")
                return None
            else:
                username = input("Username: ")
                password = input("Password: ")

    def edit_user(self, weight=None, height=None, age=None):
        # Find the user by username
        user_id = None
        for user in self.user_data['users']:
            if user['username'] == self.username:
                user_id = user['id']
                break
        if user_id is None:
            print("User not found.")
            return

        updated_fields = {}
        if weight is not None:
            updated_fields['weight'] = weight
        if height is not None:
            updated_fields['height'] = height
        if age is not None:
            updated_fields['age'] = age

        payload = {'user': updated_fields}
        response = requests.put(
            SHEETY_URL + f"users/{user_id}",
            headers=self.header_sheety,
            json=payload
        )
        if response.status_code == 200:
            print("User updated successfully.")
        else:
            print("Failed to update user:", response.text)

    def get_valid_date():
        while True:
            date_input = input("When:\nAnswer with DD/MM/YYYY format\n")
            if re.match(r"^\d{2}/\d{2}/\d{4}$", date_input):
                return date_input
            print("Invalid format. Please use DD/MM/YYYY.")

    def get_valid_time():
        while True:
            time_input = input("What Time:\nAnswer with HH:MM\n")
            if re.match(r"^\d{2}:\d{2}$", time_input):
                return time_input + ":00"
            print("Invalid format. Please use HH:MM.")
    
    def add_workout(self):
        
    


