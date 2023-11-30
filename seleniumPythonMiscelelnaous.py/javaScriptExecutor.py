from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.support.select import Select
import time

"""
imlllllllliclllllllt wait is a kind of a globa ltimeout 
if 5 sec is set max but object appear before that i will  proceed further.
"""

from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
# options.add_argument("headless") - run in headless mode
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# method to execute the javaScript
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") 
driver.get_screenshot_as_file("screen1.png")