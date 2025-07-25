import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, user_email = str, app_password = str):
        self.user_email = user_email
        self.app_password = app_password
        pass

    def send_email(self, message, target_email = None):
        if target_email is None:
            target_email = self.user_email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.user_email, password=self.app_password)
                connection.sendmail(from_addr=self.user_email, to_addrs=target_email, msg=message)
                print(f"Email to {target_email} successfully sent.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def create_message(self, destination, departure_airport, arrival_airport, price):
        message = f"Subject:Cheapest Ticket {destination}!\n\nHey, found you a great ticket for your destination.\n\nDeparture: {departure_airport}\nArrival: {arrival_airport}\nprice: ${price}\n\nGet your travel detail!\nRegards,\nAudric Satya"
        return message