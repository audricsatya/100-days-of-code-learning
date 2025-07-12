from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv("Intermediate/Day_050/.env")

FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASS")
BUTTON_TINDER_LOGIN = os.getenv("BUTTON_TINDER_LOGIN")
BUTTON_FACEBOOK_LOGIN = os.getenv("BUTTON_FACEBOOK_LOGIN")
INPUT_FACEBOOK_EMAIL = os.getenv("INPUT_FACEBOOK_EMAIL")
INPUT_FACEBOOK_PASS = os.getenv("INPUT_FACEBOOK_PASS")
BUTTON_TINDER_LOC = os.getenv("BUTTON_TINDER_LOC")
BUTTON_TINDER_NOTIF = os.getenv("BUTTON_TINDER_NOTIF")
BUTTON_TINDER_COOKIES = os.getenv("BUTTON_TINDER_COOKIES")
BUTTON_TINDER_LIKE = os.getenv("BUTTON_TINDER_LIKE")
TEXT_TINDER_MATCH = os.getenv("TEXT_TINDER_MATCH")

driver = webdriver.Chrome()
driver.get("http://www.tinder.com")

# Login Tinder
login_button = driver.find_element(By.XPATH, value=BUTTON_TINDER_LOGIN)
login_button.click()

# Login Facebook
facebook_login = driver.find_element(By.XPATH, value=BUTTON_FACEBOOK_LOGIN)
facebook_login.click()

tinder_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]

driver.switch_to.window(facebook_login_window)

email_input = driver.find_element(By.XPATH, value=INPUT_FACEBOOK_EMAIL)
email_input.send_keys(FACEBOOK_EMAIL)

password_input = driver.find_element(By.XPATH, value=INPUT_FACEBOOK_PASS)
password_input.send_keys(FACEBOOK_PASSWORD)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(tinder_window)
print(driver.title)

sleep(5)

try:
    allow_location_button = driver.find_element(By.XPATH, value=BUTTON_TINDER_LOC)
    allow_location_button.click()
    notifications_button = driver.find_element(By.XPATH, value=BUTTON_TINDER_NOTIF)
    notifications_button.click()
    cookies = driver.find_element(By.XPATH, value=BUTTON_TINDER_COOKIES)
    cookies.click()
except Exception as e:
    print(e)

for n in range(100):
    for s in range(1,3,0.5):
        sleep(s)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            BUTTON_TINDER_LIKE)
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=TEXT_TINDER_MATCH)
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()