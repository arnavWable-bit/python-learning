from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
# driver.get("https://www.amazon.com")
# driver.get("https://appbrewery.github.io/instant_pot/")
driver.get("https://python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar)
# print(search_bar.tag_name)
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value= '.documentation-widget a')
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link)


times = driver.find_elements(By.CSS_SELECTOR, value= '.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# for time in times:
#     print(time.get_attribute("datetime").split('T')[0])

# for name in names:
#     print(name.text)

events = {}
for i in range(len(times)):
    events[i] = {
            'time': times[i].get_attribute("datetime").split('T')[0],
            'name': names[i].text    
    }

print(events)

# driver.close()
driver.quit()

