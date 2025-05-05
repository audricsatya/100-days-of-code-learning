import smtplib

email = "@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()