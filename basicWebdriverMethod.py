from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
#get() - method is use to hit the url in browser.
driver.get("https://rahulshettyacademy.com")
print(driver.title) # to get the tab title

# verify that i am on correct url 
print(driver.current_url)