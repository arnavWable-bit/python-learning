import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

News_api = os.getenv("NEWS_API")
Stock_api = os.getenv("STOCK_API")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

Stock_parameters = {
    "apikey": Stock_api,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}

News_parameters = {
    "apikey": News_api,
    "q": COMPANY_NAME,
    "pageSize": 3
}

stock_response = requests.get("https://www.alphavantage.co/query", params=Stock_parameters)
stock_response.raise_for_status()
stock_data =stock_response.json()
Dict = stock_data["Time Series (Daily)"]
dict_keys = Dict.keys()
# list_keys = []
# for i in dict_keys:
#     list_keys.append(i)
list_keys = list(dict_keys)
yesterdays_closing_price= float(Dict[list_keys[0]]["4. close"])
previous_day_closing_price = float(Dict[list_keys[1]]["4. close"])
percentage = ((yesterdays_closing_price - previous_day_closing_price)/previous_day_closing_price)* 100
if percentage < 0:
    sign = "🔻"
else:
    sign = "🔺"
percentage = abs(percentage)
if percentage >= 5:
    news_response = requests.get("https://newsapi.org/v2/everything",params=News_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    client = Client(account_sid, auth_token)
    for article in articles:
        headline = f"Headline: {article["title"]}"
        brief = f"Brief: {article["description"]}"
        rise_fall = f"{STOCK}: {sign}{percentage:.2f}%"
        
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body= f"{rise_fall}\n{headline}\n{brief}\n",
        to='whatsapp:+918077585663'
        )
        
        print(message.sid)

