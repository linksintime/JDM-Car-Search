from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

PATH = "/home/asher/.local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://carfromjapan.com/")
print(driver.title)

search = driver.find_element("name", "keywords")
search.send_keys("Toyota")
search.send_keys(Keys.RETURN)

output = climage.convert('linkmotorcylcle.jpg', is_256color=True, is_unicode=True)
print(output)

try:
    carList = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-car"))
    )
    carListText = carList.text

finally:

    driver.quit()
