from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price_element = driver.find_element(By.CLASS_NAME, 'a-offscreen')

# retrieve the text from the price element
price = price_element.get_attribute('innerHTML')
print(price)

driver.quit()





#price = driver.find_elemen_by_classname "a-offscreen")
