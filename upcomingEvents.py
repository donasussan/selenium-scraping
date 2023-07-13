from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/dona/Documents/chromedriver"

chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
time_list = []
for time in time_element:
    time_value = time.text
    time_list.append(time_value)

print(time_list)

event_list = []
event_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget a")
for event in event_element:
    texts = event.get_attribute('innerHTML')
    event_list.append(texts)

event_list.remove('More')
print(event_list)

dictionary = {}
for i in range (0,5):
    dictionary_values=dict[time_list[i] : event_list[i]]
    print(dictionary_values)





driver.quit()

# price = driver.find_elemen_by_classname "a-offscreen")
