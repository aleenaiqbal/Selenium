import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome()
driver.get("https://domyassignments.ai/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)