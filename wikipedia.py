from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count_element = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#count_element.click()
#count = count_element.get_attribute('innerHTML')

search_elt = driver.find_element(By.NAME, "search")
search_elt.send_keys("Python")
search_elt.send_keys(Keys.ENTER)

import time
time.sleep(10)
driver.quit()





#price = driver.find_elemen_by_classname "a-offscreen")
