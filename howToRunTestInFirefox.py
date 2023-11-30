from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.chrome.options import Options


# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)

service_obj = Service()

# driver = webdriver.Chrome(service=service_obj,options=options)
driver = webdriver.Firefox(service=service_obj)
#maxmizethe window
driver.maximize_window()

#get() - method is use to hit the url in browser.
driver.get("https://rahulshettyacademy.com")
print(driver.title) # to get the tab title

# verify that i am on correct url 
print(driver.current_url)
# method to minimize the window
# driver.minimize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#just go back to the previous page
driver.back()
#refresh the webpage
driver.refresh()

