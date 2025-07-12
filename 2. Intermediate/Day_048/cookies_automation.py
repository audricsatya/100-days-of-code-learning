from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_argument(r'--user-data-dir=C:\Users\John\AppData\Local\Google\Chrome\User Data\SeleniumProfile')  # Windows
# chrome_options.add_argument('--user-data-dir=/home/inaya/.config/google-chrome/SeleniumProfile')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")
driver.find_element(By.ID, value='langSelect-EN').click()

def clicker(driver):
    driver.find_element(By.ID, value= 'bigCookie').click()

def get_total_cookies():
    total = int(driver.find_element(By.ID, value='cookies').text.split(" ")[0].replace(",",""))
    return total

wait_time = 5
timeout = time() + wait_time 
five_min = time() + 60 * 15

while True: 
    clicker(driver)

    if time() > timeout:
        try:
            cookies = get_total_cookies()
            
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")
        
        # Reset timer
        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break

driver.quit()

