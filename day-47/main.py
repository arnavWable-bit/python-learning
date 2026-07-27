import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
URL = "https://appbrewery.github.io/instant_pot/"
# URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

response = requests.get(URL,headers=headers)
instant_pot = response.text

soup = BeautifulSoup(instant_pot, "html.parser")
# print(soup.prettify())

price_html = soup.find(name='span', class_ = "aok-offscreen")

price = float(price_html.getText().split('$')[1])

title_html = soup.find(name='span', id='productTitle')
title = title_html.getText().strip()

TARGET_PRICE = 100

if price < TARGET_PRICE:
     with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"""Subject:Amazon Price Alert!
                {title}
                Current Price: ${price}
                Buy it here:
                {URL}
                """
            )