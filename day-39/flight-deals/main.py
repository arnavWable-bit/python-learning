#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData,find_cheapest_flight
from datetime import datetime,timedelta

tomorrow = datetime.now() + timedelta(days=1)
return_date = tomorrow + timedelta(days=7)
six_months_later = datetime.now() + timedelta(days= 180)

data_manager = DataManager()
destination_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification = NotificationManager()

for destination in destination_data:
    destination_city_code = destination["iataCode"]
    
    flights = flight_search.check_flights(origin_city_code="DEL", destination_city_code=destination_city_code, from_time=tomorrow, to_time=return_date,)

    cheapest_flight= find_cheapest_flight(flights, return_date.strftime("%Y-%m-%d"))
    if cheapest_flight.price < destination["lowestPrice"]:
        message = (
            f"✈️ Low Price Alert!\n\n"
            f"Destination: {destination['city']}\n"
            f"Price: ₹{cheapest_flight.price}\n"
            f"From: {cheapest_flight.origin_airport}\n"
            f"To: {cheapest_flight.destination_airport}\n"
            f"Departure: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )
        notification.send_whatsapp(message)

