from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv("Intermediate/Day_051/.env")

TEXT_SPEED_START = os.getenv("TEXT_SPEED_START")
TEXT_SPEED_DOWNLOAD = os.getenv("TEXT_SPEED_DOWNDLOAD")
TEXT_SPEED_UPLOAD = os.getenv("TEXT_SPEED_UPLOAD")
BUTTON_TWITTER_WELCOME = os.getenv("BUTTON_TWITTER_WELCOME")
INPUT_TWITTER_LOGIN = os.getenv("INPUT_TWITTER_LOGIN")
INPUT_TWITTER_PASSWORD = os.getenv("INPUT_TWITTER_PASSWORD")
BUTTON_TWITTER_TWEET = os.getenv("BUTTON_TWITTER_TWEET")
INPUT_TWITTER_TWEET = os.getenv("INPUT_TWITTER_TWEET")
BUTTON_TWITTER_POST = os.getenv("BUTTON_TWITTER_POST")

class InternetSpeed:
    def __init__(self):
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = Chrome(self.chrome_options)

    def speed_check(self):
        self.driver.get(url="https://www.speedtest.net")
        go_button = self.driver.find_element(By.CLASS_NAME, value=TEXT_SPEED_START)
        go_button.click()
        time.sleep(40)
        self.download = float(self.driver.find_element(By.CLASS_NAME, value=TEXT_SPEED_DOWNLOAD).text)
        self.upload = float(self.driver.find_element(By.CLASS_NAME, value=TEXT_SPEED_UPLOAD).text)
        # self.driver.quit()

    def tweet(self, user, password, message):
        time.sleep(5)
        self.driver.get(url="https://x.com")
        self.driver.maximize_window()
        time.sleep(5)
        welcome_close = self.driver.find_elements(By.CSS_SELECTOR, value=BUTTON_TWITTER_WELCOME)
        for x in welcome_close:
            x.click()
        time.sleep(5)
        login_window = self.driver.find_element(By.XPATH, value=INPUT_TWITTER_LOGIN)
        time.sleep(5)
        login_window.send_keys(user, Keys.ENTER)
        time.sleep(5)
        password_window = self.driver.find_element(By.XPATH, value=INPUT_TWITTER_PASSWORD)
        password_window.send_keys(password, Keys.ENTER)
        time.sleep(5)
        comment_window = self.driver.find_element(By.XPATH, value=BUTTON_TWITTER_TWEET)
        comment_window.click()
        self.driver.find_element(By.XPATH, value=INPUT_TWITTER_TWEET).send_keys(message)
        post_button = self.driver.find_element(By.XPATH, value=BUTTON_TWITTER_POST)
        post_button.click()

    def quit(self):
        self.driver.quit()