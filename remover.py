from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


ser = Service("C:\\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op,)


op.add_argument('--allow-running-insecure-content')
op.add_argument('--ignore-certificate-errors')
print('Выберите сервер:')
print('1 - Глобальный сервер')
print('2 - Русский сервер ')
server_enter = int(input('Ваш выбор : '))
if server_enter == 1:
   driver.get("https://sip.bas-ip.com")
elif server_enter == 2:
   driver.get("https://ru.sip.bas-ip.com")
 

assert "BAS-IP" in driver.title

email_enter = input('Введите Email от личного кабинета ')
password_enter = input('Введите Пароль от личного кабинета ')

driver.find_element(By.ID, "appbundle_login_email").send_keys(email_enter)
driver.find_element(By.ID, "appbundle_login_password").send_keys(password_enter)
driver.find_element(By.CLASS_NAME, "btn-success").click()    
    
        
count = 910


for i in range(count):
   driver.get("https://sip.bas-ip.com/family/sip-numbers/")
   driver.find_element(By.LINK_TEXT, "Редактировать").click()
   driver.find_element(By.CLASS_NAME, "btn-bold").click()
   alert_obj = driver.switch_to.alert 
   alert_obj.accept()
   time.sleep(3)
   
print(driver.title)

driver.close()
driver.quit()