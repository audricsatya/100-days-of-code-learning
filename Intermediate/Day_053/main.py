from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv("Intermediate/Day_053/.env")

GOOGLE_FORM_LINK = os.getenv('GOOGLE_FORM_LINK')
INPUT_ADDRESS = os.getenv("INPUT_ADDRESS")
INPUT_PRICE = os.getenv("INPUT_PRICE")
INPUT_LINK = os.getenv("INPUT_LINK")
BUTTON_SUBMIT = os.getenv("BUTTON_SUBMIT")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
all_links = [link["href"] for link in all_link_elements] 

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(2)

    address = driver.find_element(by=By.XPATH, 
                        value=INPUT_ADDRESS)
    price = driver.find_element(by=By.XPATH, 
                        value=INPUT_PRICE)
    link = driver.find_element(by=By.XPATH, 
                        value=INPUT_LINK)
    submit_button = driver.find_element(by=By.XPATH, 
                        value=BUTTON_SUBMIT)
    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    
    submit_button.click()