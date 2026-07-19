import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self._prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._prices_endpoint, auth=self._authorization)
        # print(response.json())
        data = response.json()
        self.destination_data = data["flightPrices"]
        return self.destination_data
    
    def get_customer_emails(self):
        response = requests.get(url=self._users_endpoint, auth=self._authorization)
        data = response.json()
        return data["users"]

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self._prices_endpoint}/{row_id}",
            json=new_data,
            auth=self._authorization
        )
