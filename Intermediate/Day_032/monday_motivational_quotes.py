import datetime as dt
import smtplib
import random

# Objective: Send a motivational email every Monday morning

# Email setup
EMAIL = "email@gmail.com" # Replace with your email
PASSWORD = "password" # Replace with your App Password
RECIPIENT_EMAIL = "email@gmail.com" # Replace with the recipient's email

def send_email(subject, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=RECIPIENT_EMAIL, 
                            msg=f"Subject:{subject}\n\n{message}")

def get_motivational_quote():
    with open("Intermediate/Day_032/quotes.txt") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

now = dt.datetime.now()

# Check if today is Monday (0 = Monday, 6 = Sunday)
if now.weekday() == 0:  # Check if today is Monday
    quote = get_motivational_quote()
    send_email("Monday Motivation", quote)
    print("Motivational email sent!")
else:
    print("Today is not Monday, no email sent.")

# Note: Ensure you have a file named "quotes.txt" with motivational quotes, one per line.