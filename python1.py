from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

link_element = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')

# retrieve the text from the price element
link = link_element.get_attribute('innerHTML')
print(link)

difficult_elt = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(difficult_elt)
driver.quit()







#price = driver.find_elemen_by_classname "a-offscreen")
