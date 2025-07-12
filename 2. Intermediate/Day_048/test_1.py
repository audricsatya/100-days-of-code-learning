from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

event_detail = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")
events = {}

for i in range(len(event_detail)):
    events[i] = {
        "time": event_detail[i].text.split("\n")[0],
        "name": event_detail[i].text.split("\n")[1]
    }

print(events)

driver.quit()
