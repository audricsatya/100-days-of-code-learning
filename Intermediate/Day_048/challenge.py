from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

firstName = driver.find_element(By.NAME, value='fName')
firstName.send_keys("sajidjioajkjd")
lastName = driver.find_element(By.NAME, value='lName')
lastName.send_keys("sadajfoa")
email = driver.find_element(By.NAME, value='email')
email.send_keys("sajdha@gmail.com")

buttonEnter = driver.find_element(By.CSS_SELECTOR, value="form button")
buttonEnter.click()

driver.quit()