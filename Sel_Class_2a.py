import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print("Navigating to me")
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 400);")
time.sleep(3)
driver.find_element(By.ID,value= "submit").click()
time.sleep(3)