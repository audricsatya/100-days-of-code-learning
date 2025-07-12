from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = int(driver.find_element(By.ID, value = "articlecount").text.split("\n")[0].split(" ")[0].replace(",",""))

driver.quit()