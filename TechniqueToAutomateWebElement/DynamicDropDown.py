from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(5)


countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
# contains list of web elements
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# get attributes of values  to validate dynamic text
# print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") =="India"
