import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)
driver.get("https://ginandjuice.shop/")
print("HELLO ALEENA")
time.sleep(5)

driver.execute_script("window.open('https://ginandjuice.shop/','_blank');") #to open in new tab
time.sleep(3)

driver.execute_script("window.open('https://ginandjuice.shop/','_blank');")
time.sleep(3)

driver.execute_script("window.open('https://ginandjuice.shop/','_blank');")
time.sleep(3)

driver.switch_to.window(driver.window_handles[0]) #1st tab
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #top=0. #bottom=full down
time.sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(3)


driver.switch_to.window(driver.window_handles[1]) #2nd tab
time.sleep(3)

driver.execute_script("window.scrollTo(0, 800);")
time.sleep(30)

driver.refresh()
time.sleep(3)

driver.maximize_window() #maximize
time.sleep(1)

driver.minimize_window() #minimize
time.sleep(1)

