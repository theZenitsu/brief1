from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()

driver.get("https://www.avito.ma/fr/immobilier")

time.sleep(3)
service = Service('C:/path/to/chromedriver.exe')


#adjust the xpath
appartments = driver.find_element(By.XPATH, "//div[@class = 'sc-1nre5ec-1 crKvIr listing']")
for appartment in appartments:
    title = appartment.find_element(By.XPATH, "//span[@class = 'sc-1x0vz2r-0 czqClV']").text
    price = appartment.find_element(By.XPATH, "//div[@class = 'sc-b57yxx-4 dRjnHr']").text
    location = appartment.find_element(By.XPATH, "//div[@class = 'sc-1x0vz2r-0 iFQpLP']").text
    












