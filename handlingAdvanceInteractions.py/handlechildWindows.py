from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

from selenium.webdriver.support.select import Select
import time

"""
imlllllllliclllllllt wait is a kind of a globa ltimeout tc
if 5 sec is set max but object appear before that i will  proceed further.
"""

from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()

driver = webdriver.Chrome(service=service_obj,options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles#handles al lthe windows which are opened
"""
The order in which the automation the tab in that order the windows get stored in list.
"""
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
# driver.close() - child window wil l close because the scope is in that window
driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)

