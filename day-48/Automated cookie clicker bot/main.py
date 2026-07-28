from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(3)

language = driver.find_element(By.ID, value= 'langSelect-EN')
language.click()
time.sleep(3)

got_it = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
got_it.click()

start_time = time.time()
next_check = start_time + 5
end_time = start_time + 60

cookie = driver.find_element(By.ID, value= 'bigCookie')

cookie_count = driver.find_element(By.ID, value= 'cookies')

while True:
    cookie.click()
    if time.time() > end_time:
        break
    if time.time() > next_check:
        cookies = cookie_count.text
        cookie_amount = int(cookies.split("\n")[0].split()[0].replace(",", ""))
        products = {}
        for i in range(20):
            product = driver.find_element(By.ID, f"product{i}")
            # price_html = driver.find_element(By.ID, f"productPrice{i}")
            # price = int(price_html.text.replace(",", ""))
            try:
                price_html = driver.find_element(By.ID, f"productPrice{i}")
                price = int(price_html.text.replace(",", ""))
                products[price] = product
            except (ValueError, NoSuchElementException):
                pass
            # products[price] = product
        affordable = []
        for price in products:
            if price <= cookie_amount:
                affordable.append(price)
        if affordable:
            highest_price = max(affordable)
            products[highest_price].click()
        next_check += 5
        
cookies = driver.find_element(By.ID, "cookies").text
print(cookies.split("\n")[1])

driver.quit()