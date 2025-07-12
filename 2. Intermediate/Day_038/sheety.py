import requests
import pandas as pd
import datetime as dt
import re

SHEETY_URL = 'https://api.sheety.co/3cb5d478ce406a3726ba20311a156646/workoutTracking/'
HOST_DOMAIN = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"

class WorkOutSheet:
    def __init__(self, sheety_token, nutritionix_token, nutritionix_app_id):
        self.header_sheety = {
            'Authorization': "Bearer " + sheety_token
        }
        self.header_nutritionix = {
            'x-app-id': nutritionix_app_id,
             'x-app-key': nutritionix_token,
        }
        self.workout_data = requests.get(SHEETY_URL+"workouts", headers=self.header_sheety).json()
        self.workout_df = pd.DataFrame(self.workout_data['workouts'])
        self.user_data = requests.get(SHEETY_URL+"users", headers=self.header_sheety).json()
        self.user_list = pd.DataFrame(self.user_data['users'])['username'].to_list()
        self.username = None


    def is_login(self):
        while True:
            choice = input("Welcome to workout tracker.\nDo you already have an account? (Y/N): ").strip().upper()
            if choice == "Y":
                username = input("Username: ")
                password = input("Password: ")
                if self.get_user(username,password):
                    print(f"Welcome, {self.username}!")
                    break
            elif choice == "N":
                self.create_user()
                print("Account created. Please relogin.")
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
                
    def check_username(self,username):
        while True:
            if username in self.user_list:
                username = input("username already taken.\nEnter other username: ")
            else:
                print("username available")
                return username

    def create_user(self):
        username = input("Enter your username: ").lower()
        username = self.check_username(username)
        name = input("Enter your name: ")
        height = input("Enter your height: ")
        weight = input("Enter your weight: ")
        age = input("Enter your age: ")
        password = input("Enter your password:\n(Do Not Forget. Contact admin if you are.)\n")
        
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

        user_request = requests.post(SHEETY_URL+"users", headers=self.header_sheety, json=new_user)
        user_request.raise_for_status()

    def get_user(self, username, password):
        for user in self.user_data['users']:
            if user['username'] == username.lower() and user['password'] == password:
                print("Login successful.")
                self.username = username 
                self.name = user['name']
                self.weight = user['weight']
                self.height = user['height']
                self.age = user['age']
                return True
            elif user['username'] == username and user['password'] != password:
                print("Password is Invalid")
        print("User not Found")
        return False

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

    def get_valid_date(self):
        while True:
            date_input = input("When:\nAnswer with DD/MM/YYYY format (leave blank for today)\n")
            if not date_input:
                return dt.datetime.now().strftime("%d/%m/%Y")
            if re.match(r"^\d{2}/\d{2}/\d{4}$", date_input):
                return date_input
            print("Invalid format. Please use DD/MM/YYYY.")

    def get_valid_time(self):
        while True:
            time_input = input("What Time:\nAnswer with HH:MM (leave blank if you are forget)\n")
            if not time_input:
                return "12:00:00"
            if re.match(r"^\d{2}:\d{2}$", time_input):
                return time_input + ":00"
            print("Invalid format. Please use HH:MM.")
    
    def add_workout(self, message = str):
        DATE = self.get_valid_date()
        TIME = self.get_valid_time()
        
        nutritionix_parameters = {
            'query': message,
            'weight_kg': self.weight,
            'height_cm': self.height,
            'age': self.age
        }

        nutritionix_request = requests.post(HOST_DOMAIN+END_POINT, headers=self.header_nutritionix, json=nutritionix_parameters)
        data_nutritionix_json = nutritionix_request.json()

        for data_exercise in data_nutritionix_json['exercises']:
            new_data = {'workout':
                        {
                    'date':DATE,
                    'time':TIME,
                    'exercise': data_exercise['name'].title(),
                    'duration': data_exercise['duration_min'],
                    'calories': data_exercise['nf_calories'],
                    'user': self.username
                }
            }
            print(new_data)

            add_workout_data = requests.post(SHEETY_URL+"workouts", json=new_data, headers=self.header_sheety)
            add_workout_data.raise_for_status()

    def get_workout_data(self):
        print(f"Hello {self.name}\n")
        user_workout = self.workout_df[self.workout_df['user']==self.username]
        print(user_workout)
        print("Dont forget to workout!")