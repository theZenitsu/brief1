from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()

all_url = "https://www.avito.ma/fr/maroc/appartments"
driver.get(all_url)

links = []

for i in range(1, 9):  # Loop through pages 1 to 8
        # Wait for the page to load (adjust as needed)
        time.sleep(10)
        
        # Find all anchor tags with href attributes using XPath
        page_links = [a.get_attribute('href') for a in driver.find_elements(By.XPATH, "//a[@href = '']")]
        
        # Add to the main links list
        links.extend(page_links)

print(page_links)

driver.quit()