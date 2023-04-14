import openpyxl
import pandas as pd
import json
import shutil


wb = openpyxl.load_workbook('SIP_SORT2.xlsx')

dict_sapmple_json = []
dict_sapmple_exel = {}
counts = 0

# печатаем список листов
sheets = wb.sheetnames

for sheet in sheets:
    sheet = wb.active

for row in sheet.values:
    # Новый кортеж 1  (все элементы с 0 индекса через 1 значение)
    newtuple = row[3::] 
    # Новый кортеж 2 (все элементы с 1 индекса через 1 значение)
    newtuple2 = row[0::]
    # Обьеденяем два ровнозаначных!!! кортежа
    lister = zip(newtuple, newtuple2)
    for numbers, value_sip in lister:
        counts += 1
        # Итерация в список
        dict_ = { 'apartment': numbers, 'forward_numbers':[value_sip]}      
        dict_sapmple_json.append(dict_)
        # Итерация в словарь
        dict_exel = {numbers:value_sip}
        dict_sapmple_exel.update(dict_exel)

# Сохранем в Exel Pandas
# df = pd.DataFrame.from_dict(dict_sapmple_exel,'index').reset_index()
# df.columns = ['Квартира', 'SIP']
# df.to_excel('SIP_SORT.xlsx', index=False)   

# Сохраняем в JSON
json_result = {'count':counts, 'items':dict_sapmple_json, 'version':1}
# Открвыем файл json на запись
with open("data_file.json", "w") as write_file:
    json.dump(json_result, write_file)

shutil.copy('data_file.json', 'forwards.json')

print('=== OK ! is GOOD ===')




        




        
        
   
    

 