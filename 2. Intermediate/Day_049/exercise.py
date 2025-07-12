from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv("Intermediate/Day_049/.env")

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
PHONE = os.getenv("PHONE_NUMBER")

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)

try:
    driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button').click()
except Exception as e:
    print(e)

#Login
input_username = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
input_password = driver.find_element(By.ID, value="base-sign-in-modal_session_password")

input_username.send_keys(EMAIL)
input_password.send_keys(PASSWORD)
driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button').click()

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    try:
        listing.click()
        time.sleep(2)
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]").text
        # if phone.text == "":
            # phone.send_keys(PHONE)

        next_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        next_button.click()
        time.sleep(2)

        review_button = driver.find_element(By.CSS_SELECTOR, 'button[data-live-test-easy-apply-review-button]')
        review_button.click()
        time.sleep(2)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[data-live-test-easy-apply-submit-button]')
        submit_button.click()
        time.sleep(2)
        
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
            
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

    except Exception as e:
        continue

driver.quit()