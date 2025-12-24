import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(3)


 #Using XPATH

"""driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.find_element(By.XPATH,"////input[@name='login-button']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='user-name']").click()
time.sleep(3)"""

"""driver.find_element(By.XPATH,"//input[@type='submit']").click() #Find specific place
time.sleep(3)"""

"""driver.find_element(By.XPATH,"//input[@id='password']").click()
time.sleep(3)"""

"""driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.find_element(By.XPATH,"//*[contains(@name,'user-name')]").click() #find in full DOM"""

#//div[text()="Swag Labs"] find text

driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
time.sleep(3)


driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(3)