import pandas as pd
import smtplib
import datetime as dt
import random

# Objective: Send birthday wishes via email if today matches a birthday in the CSV file
# Note: Ensure you have a file named "birthdays.csv" with columns "name", "email", "day", "month"

# Email setup
EMAIL = "email@gmail.com"  # Replace with your email
PASSWORD = "password"  # Replace with your App Password
SENDER_NAME = "Sender"  # Replace with your name

# 1. Read birthdays.csv
birthdays_df = pd.read_csv("Intermediate/Day_032/birthday_wisher/birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)
today_birthdays = birthdays_df[(birthdays_df['month'] == today[0]) & (birthdays_df['day'] == today[1])]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not today_birthdays.empty:
    # Load letter templates
    with open("Intermediate/Day_032/birthday_wisher/letter_templates/letter_1.txt") as file1, \
         open("Intermediate/Day_032/birthday_wisher/letter_templates/letter_2.txt") as file2, \
         open("Intermediate/Day_032/birthday_wisher/letter_templates/letter_3.txt") as file3:
        letters = [file1.read(), file2.read(), file3.read()]

    letter_template = random.choice(letters)

# 4. Send the letter generated in step 3 to that person's email address.

    # Send birthday wishes via email
    for index, row in today_birthdays.iterrows():
        name = row['name']
        email = row['email']
        personalized_letter = letter_template.replace("[NAME]", name).replace("[SENDER_NAME]", SENDER_NAME)    

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday {name}!\n\n{personalized_letter}"
            )
        print(f"Birthday email sent to {name} at {email}")





