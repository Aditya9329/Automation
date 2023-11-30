from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://rahulshettyacademy.com/angularpractice/")


# locators to find element - ID,CSSSelector,name,linktext,XPATH
"""find_element - to get the element
send_keys() - to send inputs to the field"""
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
#CSSSelector
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rohan")
# XPATH syntax - //tagname[@attribute='value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
# text() - use to grab the text
message = driver.find_element(By.CLASS_NAME,"alert").text
print(message)

assert "Success" in message
