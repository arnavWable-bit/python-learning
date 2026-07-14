import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
api_key = os.getenv("OPENWEATHER_API_KEY")

parameters = {
    "lat":7.086170,
    "lon":-70.757347,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body= "It's going to rain today.\nRemember to bring an ☔️",
    to='whatsapp:+918077585663'
    )

    print(message.sid)