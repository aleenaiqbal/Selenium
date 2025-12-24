import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome()
driver.get("https://crm.internalcreatics.com/login")
time.sleep(1)

driver.maximize_window()
time.sleep(1)
"""
#TESTCASE: 1 To check the WelcomeText
Text= driver.find_element(By.CLASS_NAME,"mb-2").text
print(Text)
time.sleep(1)
if Text == "welcome back !":
    print("PASSED")
else:
    print("FAILED")
"""
#Testcase: 2 Blank Fields

driver.find_element(By.XPATH,'//*[@id="login_from"]/div/div[3]/button').click()
time.sleep(30)

error_blank = driver.find_element(By.CLASS_NAME, "text-danger").text
print("Error Message:", error_blank)
time.sleep(1)

if "required" in error_blank.lower():
    print("PASSED")
else:
    print("FAILED")
