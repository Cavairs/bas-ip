from bs4 import BeautifulSoup as soup
import requests
import pandas as pd


session = requests.Session()

link = 'https://sip.bas-ip.com/login_check'

data ={
    'appbundle_login[email]': 'pikasso1k1@yandex.ru',
    'appbundle_login[password]': '112274'
}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

rest = session.post(link, data=data, headers=header).text

page = 1
sip1 = []
sip2 = []
sip3 = []
dic_sip = {}

while True:
    profile_info = 'https://sip.bas-ip.com/family/sip-numbers/?page=' +str(page) 
    profile_response = session.get(profile_info, headers=header).text
    html = soup(profile_response, 'lxml')
    sip = html.find('table', class_='table').find_all('td')  

    if (len(sip)):
       for sip_number in sip[::5]:
           sip1.append(sip_number.text)
       for sip_name in sip[1::5]:
           sip2.append(sip_name.text)
       for sip_pass in sip[2::5]:
           sip3.append(sip_pass.text)                 
    else:
        break          
    page += 1
dic_sip = {sip1[i]: [sip2[i], sip3[i]] for i in range(len(sip1))}     

print(dic_sip)

# Сохранем в Exel Pandas
df = pd.DataFrame.from_dict(dic_sip,'index').reset_index()
df.columns = ['Sip номер', 'Квартира', 'Пароль']
df.to_excel('SIP_SORT2.xlsx', index=False)   
       


# URL = 'https://sip.bas-ip.com/family/sip-numbers/'
# page = requests.get(URL)

# soup = BeautifulSoup(page.text, "html.parser")

# print(soup)