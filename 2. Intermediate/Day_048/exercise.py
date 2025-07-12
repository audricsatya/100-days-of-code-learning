from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https:\\www.amazon.com")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")
# driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]').text.replace("\n",".")

# Learning
# Name
# driver.find_element(By.NAME, value="q").get_attribute("placeholder")
# ID
# driver.find_element(By.ID, value="submit").size
# CSS (".class anchor_tag")
# driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text
# XPATH
# driver.find_element(By.XPATH, value="copy xpath value from inspect elements")

# Click
# driver.find_element(By. .... , value = "").click()
# or
# driver.find_element(By.LINK_TEXT , value = "Visible Text Name").click()

# Search
# search_bar = driver.find_element(By.NAME , value = "search")
# search_bar.sent_keys("TEXT", Keys.ENTER)

driver.quit()
