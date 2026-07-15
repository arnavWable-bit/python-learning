import requests
from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

import os

load_dotenv()

X_API_ID = os.getenv("X_APP_ID")
X_APP_KEY = os.getenv("X_APP_KEY")
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASS = os.getenv("SHEETY_PASS")

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": X_API_ID,
    "x-app-key": X_APP_KEY
}

data = {
    "query": exercise_text
}

response = requests.post(url=exercise_endpoint, headers=headers, json=data)
result = response.json()
calories= result['exercises'][0]['nf_calories']
duration= result['exercises'][0]['duration_min']
exercise= result['exercises'][0]["name"].title()

Sheety_endpoint = "https://api.sheety.co/fc01cc70d7e36c44625bf156eac039b2/workoutTracking/workouts"

today = datetime.now()

sheety_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

basic = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASS)

sheety = requests.post(url=Sheety_endpoint,json=sheety_data, auth=basic)
print(sheety.json())
