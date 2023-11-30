from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# if not attribute defined then this is the way- //form/div[1]/input
# form div:nth-child(2) input - CSS
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("1234")

driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("1234")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()



