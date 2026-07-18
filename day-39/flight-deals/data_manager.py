import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/fc01cc70d7e36c44625bf156eac039b2/flightDeals/flightPrices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_PASS = os.getenv("SHEETY_PASS")
        self.SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
        self.destination_data = []
        
    def get_destination_data(self):
        basic = HTTPBasicAuth(self.SHEETY_USERNAME, self.SHEETY_PASS)
        response = requests.get(url= SHEETY_ENDPOINT, auth=basic)
        response.raise_for_status()
        self.destination_data = response.json()["flightPrices"]
        return self.destination_data