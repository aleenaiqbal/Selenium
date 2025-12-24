""" write this on terminal
pip install selenium
pip show selenium"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options #To access chrome option
options = Options()

options.add_argument('--incognito') #To open in incognito
options.add_argument('--headless') #the browser runs without UI

driver = webdriver.Chrome(options=options) #shoild pass option here for chrome access
print("Navigate to web")
driver.get("https://ginandjuice.shop/") #get is used to open browser
print("Navigate to web")
time.sleep(3) #delay