class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        
def find_cheapest_flight(data, return_date):
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])
    try:
        cheapest_flight = all_flights[0]
        for flight in all_flights:
            if flight["price"] < cheapest_flight["price"]:
                cheapest_flight = flight
    except IndexError:
        return FlightData(
            "N/A",
            "N/A",
            "N/A", 
            "N/A",
            "N/A"
        )
    price = cheapest_flight["price"]
    origin_airport = cheapest_flight["flights"][0]["departure_airport"]["id"]
    destination_airport = cheapest_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = cheapest_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
    return FlightData(
        price,
        origin_airport,
        destination_airport,
        out_date,
        return_date,
    )