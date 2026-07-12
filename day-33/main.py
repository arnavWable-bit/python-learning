import requests
import datetime as dt

MY_LAT = 12.966093
MY_LONG = 79.165357

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# # print(response.status_code)
# # if response.status_code == 404:
# #     raise Exception("The resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data.")


# # Instead of writing so many if statements 
# response.raise_for_status()

# # data = response.json()
# # data = response.json()['iss_position']
# # print(data)

# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
# iss_position = (longitude,latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise)
print(sunrise.split('T')[1].split(":")[0])

time_now = dt.datetime.now()
# print(time_now)