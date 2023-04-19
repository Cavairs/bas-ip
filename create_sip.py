from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
 
# Указываем полный путь к geckodriver.exe на вашем ПК.
# EXE_PATH = r'pa\to\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=EXE_PATH)

# start_string = "43k1kv"
# count = 10
# result = []

# def generate_string(start_string, count):
#     for i in range(count):
#         result.append(start_string + str(i+1))
#         return start_string + str(i+1)
# print(generate_string(start_string, count))

# for string in generate_string(start_string, count):
#     print(result)


ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op,)

op.add_argument('--allow-running-insecure-content')
op.add_argument('--ignore-certificate-errors')

driver.get("https://sip.bas-ip.com")
assert "BAS-IP" in driver.title
# element = driver.find_element_by_id ('appbundle_login_email')
driver.find_element(By.ID, "appbundle_login_email").send_keys("skandinavskybulvar.19@gmail.com")
driver.find_element(By.ID, "appbundle_login_password").send_keys("A101a101")
driver.find_element(By.CLASS_NAME, "btn-success").click()    
    
         
start_number = 1
count = 628

for i in range(count):
    string = "19kv"
    number = start_number + i
    driver.get("https://sip.bas-ip.com/family/sip-numbers/new")
    driver.find_element(By.ID, "appbundle_sipnumber_name").send_keys(string + str(number))
    driver.find_element(By.ID, "appbundle_sipnumber_password").send_keys('A123456a')
    driver.find_element(By.CLASS_NAME, "btn-success").click()
    
    





print(driver.title)
time.sleep(10)
driver.close()
driver.quit()



# for string in generate_string(start_string, count):
#     print(string)