from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv("Intermediate/Day_52/.env")

BUTTON_INSTAGRAM_COOKIES = load_dotenv("BUTTON_INSTAGRAM_COOKIES")
INPUT_INSTAGRAM_USERNAME = load_dotenv("INPUT_INSTAGRAM_USERNAME")
INPUT_INSTAGRAM_PASSWORD = load_dotenv("INPUT_INSTAGRAM_PASSWORD")
BUTTON_INSTAGRAM_LOGIN_SAVED = load_dotenv("BUTTON_INSTAGRAM_LOGIN_SAVED")
BUTTON_INSTAGRAM_NOTIFICATION = load_dotenv("BUTTON_INSTAGRAM_NOTIFICATION")
SCRIPT_INSTAGRAM_MODAL = load_dotenv("SCRIPT_INSTAGRAM_MODAL")
BUTTON_INSTAGRAM_ALL = load_dotenv("BUTTON_INSTAGRAM_ALL")
BUTTON_INSTAGRAM_CANCEL = load_dotenv("BUTTON_INSTAGRAM_CANCEL")

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4)

        decline_cookies_xpath = BUTTON_INSTAGRAM_COOKIES
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        input_username = self.driver.find_element(by=By.NAME, value=INPUT_INSTAGRAM_USERNAME)
        input_password = self.driver.find_element(by=By.NAME, value=INPUT_INSTAGRAM_PASSWORD)

        input_username.send_keys(username)
        input_password.send_keys(password)

        time.sleep(2)
        input_password.send_keys(Keys.ENTER)

        time.sleep(4)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value=BUTTON_INSTAGRAM_LOGIN_SAVED)
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value=BUTTON_INSTAGRAM_NOTIFICATION)
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self,target_user):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{target_user}/followers")

        time.sleep(9)
        modal_xpath = SCRIPT_INSTAGRAM_MODAL
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value=BUTTON_INSTAGRAM_ALL)

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value=BUTTON_INSTAGRAM_CANCEL)
                cancel_button.click()

    def quit(self):
        self.driver.quit()