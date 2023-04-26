from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
import random
import string
 
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
    
         
start_number = 629  # указываем с какой квартиры начинать
count = int(input('Укажите колчисество квартир '))  # указываем количество квартир
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number_pass = 1
length = 3  # длина пароля  (Плюс три символа)
number_pass = int(number_pass)
length = int(length)

for i in range(count):
    my_string = "19kv"
    number = start_number + i
    if server_enter == 1:
        driver.get("https://sip.bas-ip.com/family/sip-numbers/new")
    elif server_enter == 2:
        driver.get("https://ru.sip.bas-ip.com/family/sip-numbers/new")    
    driver.find_element(By.ID, "appbundle_sipnumber_name").send_keys(my_string + str(number))
    for n in range(number_pass):
        password = str(random.randint(0, 9))
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        print(password)
        for x in range(length):
            password += random.choice(chars)
    driver.find_element(By.ID, "appbundle_sipnumber_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn-success").click()


print(driver.title)
time.sleep(10)
driver.close()
driver.quit()







    #         password += str(random.randint(0, 9))
    #         print(password)

    # # Добавить одну случайную маленькую букву
    #         password += random.choice(string.ascii_lowercase)
    #         print(password)

    # # Добавить одну случайную большую букву
    #         password += random.choice(string.ascii_uppercase)

    # # Добавить остальные случайные символы
    #         password += ''.join(random.sample(string.ascii_letters + string.digits, length - 3))