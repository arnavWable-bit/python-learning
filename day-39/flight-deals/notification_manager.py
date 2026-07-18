from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

class NotificationManager():
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
    def send_whatsapp(self, message):
        self.client.messages.create(
            from_='whatsapp:+14155238886',
            body= f"{message}",
            to='whatsapp:+918077585663'
        )