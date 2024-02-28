import os
import smtplib
from twilio.rest import Client

TWILIO_SID = 'AC0a7b15c571d4fcc70a5677e8a22b0576'
TWILIO_AUTH_TOKEN = '1f9be237aa8a151685d5ea2ce9ae2095'
TWILIO_VIRTUAL_NUMBER = '+19797107336'
TWILIO_VERIFIED_NUMBER = '+16476876016'
my_email = "eve96871@gmail.com"
password = "pegaauthpsijeitk"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            from_= TWILIO_VIRTUAL_NUMBER,
            to= TWILIO_VERIFIED_NUMBER,
            body=message
        )
        print(message.sid)

    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            for email in emails:
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:New low price flight!\n\n{message}".encode('utf-8'))
