from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

ACCOUNT_EMAIL = "Wable@test.com"
ACCOUNT_PASSWORD = "Wablearnav"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "day-49/Automated exercise routine at gym/chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(chrome_options)
driver.get(GYM_URL)

def retry(func, retries=7, description=None):
    for attempt in range(retries):
        try:
            result = func()
            print(f"✓ {description} successful")
            return result
        except Exception as e:
            print(f"{description} Attempt {attempt + 1} failed: {e}")
        
    raise Exception(f"Failed after {retries} attempts")

def login():
    login = driver.find_element(By.ID, value= 'login-button')
    login.click()

    # email = driver.find_element(By.ID, value= 'email-input')
    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email-input"))
    )
    email.clear()
    email.send_keys(ACCOUNT_EMAIL)

    password = driver.find_element(By.ID, value= 'password-input')
    password.clear()
    password.send_keys(ACCOUNT_PASSWORD)

    submit = driver.find_element(By.ID, value= 'submit-button')
    submit.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "schedule-page"))
    )

retry(login, description="Login")

# class_times = driver.find_elements(
#     By.CSS_SELECTOR,
#     "p[id^='class-time-']"
# )
# for class_time in class_times:
#     print(class_time.text)

def book_class(button):
    old_text = button.text
    button.click()
    WebDriverWait(driver, 10).until(
        lambda d: button.text != old_text
    )
    
    
day_groups = driver.find_elements(By.CSS_SELECTOR, "[id^='day-group-']")

# for day in day_groups:
#     print(day.get_attribute("id"))

booked_count = 0
waitlist_count = 0
already_booked_count = 0
already_waitlisted_count = 0

processed_classes = []

for day in day_groups:
    heading = day.find_element(By.TAG_NAME, "h2")
    if "Tue" in heading.text or "Thu" in heading.text:
        class_times = day.find_elements(
            By.CSS_SELECTOR,
            "p[id^='class-time-']"
        )

        for class_time in class_times:
            if "6:00 PM" in class_time.text:
                parent = class_time.find_element(By.XPATH, "..")
                card_content = parent.find_element(By.XPATH, "..")
                card = card_content.find_element(By.XPATH, "..")
                button = card.find_element(By.TAG_NAME, "button")
                class_name = card.find_element(By.TAG_NAME, "h3")
                
                is_booked = card.get_attribute("data-user-booked")
                is_waitlisted = card.get_attribute("data-user-waitlisted")
                if is_booked == "true":
                    print(f"✓ Already booked: {class_name.text} on {heading.text}")
                    already_booked_count += 1
                    processed_classes.append(
                        f"[Already Booked] {class_name.text} on {heading.text}"
                    )
                elif is_waitlisted == "true":
                    print(f"✓ Already on waitlist: {class_name.text} on {heading.text}")
                    already_waitlisted_count += 1
                    processed_classes.append(
                        f"[Already Waitlisted] {class_name.text} on {heading.text}"
                    )
                elif button.text == "Book Class":
                    # button.click() 
                    retry(lambda: book_class(button), description="Booking class")
                    print(f"✓ Booked: {class_name.text} on {heading.text}")
                    booked_count += 1
                    processed_classes.append(
                        f"[New Booking] {class_name.text} on {heading.text}"
                    )
                elif button.text == "Join Waitlist":
                    #button.click()
                    retry(lambda: book_class(button), description="Booking class")
                    print(f"✓ Joined waitlist: {class_name.text} on {heading.text}")
                    waitlist_count += 1
                    processed_classes.append(
                        f"[New Waitlist] {class_name.text} on {heading.text}"
                    )
                    
already_count = already_booked_count + already_waitlisted_count
total_classes = booked_count + waitlist_count + already_count

print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_count}")
print(f"Total Tuesday & Thursday 6pm classes: {total_classes}")

print("\n--- DETAILED CLASS LIST ---")
for class_info in processed_classes:
    print(f"  • {class_info}")
    
def get_my_bookings():
    my_bookings = driver.find_element(By.ID, "my-bookings-link")
    my_bookings.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "my-bookings-page"))
    )
    booking_cards = driver.find_elements(
        By.CSS_SELECTOR,
        "[id^='booking-card-']"
    )
    return booking_cards

booking_cards = retry(get_my_bookings, description="Getting bookings")

verified_count = 0

for booking in booking_cards:
    if ("Tue" in booking.text or "Thu" in booking.text) and "6:00 PM" in booking.text:
        class_name = booking.find_element(By.TAG_NAME, "h3")
        print(f"✓ Verified: {class_name.text}")
        verified_count += 1
        
print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_classes} bookings")
print(f"Found: {verified_count} bookings")

if verified_count == total_classes:
    print("✅ SUCCESS: All bookings verified!")
else:
    difference = total_classes - verified_count
    print(f"❌ MISMATCH: Missing {difference} bookings")