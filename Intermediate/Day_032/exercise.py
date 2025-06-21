import smtplib

email = "email@gmail.com"
password = "password" # Note: Replace with your actual email and password from App Password.

# For Gmail, you need to enable "Less secure app access" or use an App Password if 2FA is enabled.
# Make sure to use an App Password if you have 2FA enabled on your account.

designation_email = "email@gmail.com"  # Replace with the recipient's email address
subject = "Hello"
message = """Subject:Hello\n\nThis is the body of the email."""

# Option 1
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=designation_email, 
    msg=message)
connection.close()

# Option 2
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=designation_email, 
        msg=message)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()