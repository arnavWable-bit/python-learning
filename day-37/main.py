import requests
from datetime import datetime
from dotenv import load_dotenv

import os

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "learning graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2"

# today = datetime(year=2026, month=7, day=14)
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)


# UPDATING YESTERDAYS DATA , USED 6 HOURS UPDATING TO 8

pixel_update = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2/{today.strftime("%Y%m%d")}"


pixel_update_config = {
    "quantity": "10"
}

# response = requests.put(url=pixel_update, json=pixel_update_config, headers=headers)
# print(response.text)


# DELETING A PIXEL

pixel_delete = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph2/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=pixel_delete, headers=headers)
# print(response)