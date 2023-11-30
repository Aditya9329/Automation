from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
import time

"""
imlllllllliclllllllt wait is a kind of a globa ltimeout 
if 5 sec is set max but object appear before that i will  proceed further.
"""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
# time.sleep(5)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(results))
assert len(results) > 0 

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(10)
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
