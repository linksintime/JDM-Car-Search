from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

# PARAMETERS
search_key = "Nissan 180sx"

PATH = "/home/asher/.local/bin/chromedriver"
options = Options()
options.add_argument("--headless") # No web page is loaded. Doesn't have to open chromium
driver = webdriver.Chrome(PATH ,options=options)
list_of_cars = []

driver.get("https://carfromjapan.com/")
print(driver.title)

search = driver.find_element("name", "keywords")
search.send_keys(search_key)
search.send_keys(Keys.RETURN)


try:
    carTab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-car"))
    )
    carRow = carTab.find_elements(By.CLASS_NAME, "car-row")

    for rows in carRow: # Scrapes information about cars listings in car-row class and sorts it into a list
        carlistings = list(rows.text.split("\n"))
        list_of_cars.append(carlistings)

    for cars in list_of_cars: # Beautiful view of those very lists
        print(cars)

finally:

    driver.quit()
