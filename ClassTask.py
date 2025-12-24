import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()

list_URL =  ["https://assignmenthelpsingapore.com.sg",
    "https://financeassignmenthelper.co.uk/",
    "https://domyonlineclasshelp.com/"]

options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

for url in list_URL:
    driver.get(url)

time.sleep(2)