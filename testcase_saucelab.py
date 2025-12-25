import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--guest')
driver=webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
time.sleep(3)

driver.maximize_window()

#TESTCASE: 1 To check heading

Text= driver.find_element(By.CLASS_NAME,"login_logo").text
print(Text)
time.sleep(1)
if Text == "Swag Labs":
    print("PASSED")
else:
    print("FAILED")

#Testcase: 2 Blank Fields

driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(3)

Username = driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Username)
print(Username)
time.sleep(3)
if Username == "Epic sadface: Username is required":
    print("PASSED")

else:
    print("FAILED")



#TestCase: 3 Username enter to check password validation


driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(3)

val2=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(val2)
time.sleep(3)
if val2 == "Epic sadface: Password is required":
    print("PASSED")

else:
    print("FAILED")
driver.refresh()

#Testcase: 4 Enter Password to check username

driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(2)
val3=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(val3)
time.sleep(3)
if val3 == "Epic sadface: Username is required":
    print("PASSED")

else:
    print("FAILED")

driver.refresh()

#Testcase: 5 Correct username and incorrect password

driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("hello")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(3)

val4=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(val4)
time.sleep(3)
if val4 == "Epic sadface: Username and password do not match any user in this service":
    print("PASSED")

else:
    print("FAILED")
driver.refresh()


#Testcase: 6 Login successfully

driver.find_element(By.CSS_SELECTOR,"[placeholder=Username]").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"[placeholder=Password]").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR,'#login-button').click()
time.sleep(5)


#TestCase: 7 Add Product
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-fleece-jacket').click()
time.sleep(3)

price = driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text
print(price)
newp= price.replace("$","")
print(type(newp))
print(newp)
ip = float(newp)
print(type(ip))
print(ip)

time.sleep(3)

print()

driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bolt-t-shirt').click()
time.sleep(3)

price2 = driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div').text
print(price2)
newp2= price2.replace("$","")
print(type(newp2))
print(newp2)
ip2 = float(newp2)
print(type(ip2))
print(ip2)


driver.find_element(By.CSS_SELECTOR,'#remove-sauce-labs-bolt-t-shirt').click()
time.sleep(3)




driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(3)

#Testcase: 8 Go To cart
driver.find_element(By.CSS_SELECTOR,'[class=shopping_cart_container]').click()
time.sleep(3)

#TESTCASE: 9 Continue Shopping
driver.find_element(By.XPATH,'//button[@id="continue-shopping"]').click()
time.sleep(3)

#TESTCASE: 10 Add One more product
driver.find_element(By.CSS_SELECTOR,'#add-to-cart-sauce-labs-bike-light').click()
time.sleep(3)

price3 = driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div').text
print(price3)
newp3= price3.replace("$","")
print(type(newp3))
print(newp3)
ip3 = float(newp3)
print(type(ip3))
print(ip3)
time.sleep(3)



#TESTCASE: 11 Go To Cart

driver.find_element(By.CSS_SELECTOR,'[class=shopping_cart_container]').click()
time.sleep(3)

driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'#checkout').click()
time.sleep(3)

"""
#TESTCASE: 12 Condition check using assert 

Text= driver.find_element(By.CLASS_NAME,"login_logo").text
print(Text)
time.sleep(1)
assert Text == "Swag Labs"
"""

#TESTCASE: 13   Add firstname

driver.find_element(By.CSS_SELECTOR,'#first-name').send_keys("ALEENA")
driver.find_element(By.CSS_SELECTOR,'#last-name').send_keys("IQBAL")
driver.find_element(By.CSS_SELECTOR,'#postal-code').send_keys("12345")
driver.find_element(By.CSS_SELECTOR,'#continue').click()
time.sleep(3)


# TESTCASE: 14 Verify total price calculation
p_price = [ip, ip3]
total_price = sum(p_price)
print("Calculation total price",total_price)

item_total_price = driver.find_element(By.CSS_SELECTOR,'[class=summary_subtotal_label]').text
print(item_total_price)
time.sleep(3)


# Remove text + dollar sign
ui_total = item_total_price.replace("Item total: $", "")
ui_total = float(ui_total)

print("UI Total:", ui_total)

# Correct comparison
if total_price == ui_total:
    print("PASSED")
else:
    print("FAILED")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight );")
time.sleep(3)
time.sleep(3)


#Testcase: 15 verify tax

tax = round(ui_total * 0.08,2)
print("Calculated Tax:", tax)

tax_text = driver.find_element(By.CSS_SELECTOR,'[class=summary_tax_label]').text
print("UI TAX TEXT: ",tax_text)

ui_tax = float(tax_text.replace("Tax: $", ""))
print("UI TAX:", ui_tax)
if round(tax, 2) == round(ui_tax, 2):
    print("PASSED")
else:
    print("FAILED")
time.sleep(3)

#testcase: 16 Click on Finish Button
driver.find_element(By.CSS_SELECTOR,'#finish').click()
time.sleep(3)






