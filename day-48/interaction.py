from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page/")
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

# number_of_aricles = driver.find_element(By.ID, value= 'mwDw')
# number_of_aricles.click()

# Find element by LINK_TEXT
# all_portals = driver.find_element(By.LINK_TEXT, value= 'Content portals')
# all_portals.click()


# Find the "search" <input> by Name
# search = driver.find_element(By.NAME, value= 'search')

# Sending keyboard input to selenium
# search.send_keys('Python', Keys.ENTER)

fname = driver.find_element(By.NAME, value= 'fName')
fname.send_keys('Arnav')
lname = driver.find_element(By.NAME, value= 'lName')
lname.send_keys('Wable')
email = driver.find_element(By.NAME, value= 'email')
email.send_keys('afegedged@gmail.com')

button = driver.find_element(By.CLASS_NAME, value="btn-primary")
button.send_keys(Keys.ENTER)

driver.quit()


