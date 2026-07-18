import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERP_ENDPOINT = "https://serpapi.com/search.json"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["SERP_API_KEY"]
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "api_key": self._api_key,
            "engine": "google_flights",
            # "departure_id": "DEL",
            # "arrival_id": "AUS",
            "currency": "INR",
            "type": 1,
            "adults": 1
        }
        params["arrival_id"] = destination_city_code
        params["departure_id"] = origin_city_code
        params["outbound_date"] = from_time.strftime("%Y-%m-%d")
        params["return_date"] = to_time.strftime("%Y-%m-%d")
        response = requests.get(url=SERP_ENDPOINT,params=params )
        response.raise_for_status()
        data = response.json()
        return data