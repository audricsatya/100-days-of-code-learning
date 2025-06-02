import smtplib

email = "@gmail.com"
password = "your_password"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=email, 
    msg="Subject:Hello\n\nThis is the body of the email.")