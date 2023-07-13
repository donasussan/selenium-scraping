from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")


first_elt = driver.find_element(By.NAME, "fName")
first_elt.send_keys("Dona Sussan")
second_elt = driver.find_element(By.NAME, "lName")
second_elt.send_keys("Chacko")
email_elt = driver.find_element(By.NAME, "email")

email_elt.send_keys("donasussan@gmail.com")

email_elt.send_keys(Keys.ENTER)


import time
time.sleep(15)
driver.quit()





#price = driver.find_elemen_by_classname "a-offscreen")
