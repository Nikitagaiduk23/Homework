import requests
#Імпортуваня бібліотеки Requests 
from .read_json import read_json
#Імпортує функцію для читання json файлів
import json
#Імпортуваня json
data_api = read_json(name_file= 'config_api.json')
#Копіювання вміста файла config_api 
API_KEY = data_api['api_key']
#Константа зі значенням api ключа
CITY_NAME = data_api['city_name']
#Константа з ім'ям міста
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Константа з посиланням у яку ми передаемо константи CITY_NAME та API_KEY 
response = requests.get(URL)
#отримує дані за посиланням URL
if response.status_code == 200:
    #Умова яка перевіряє чи були отрімані данні
    data_dict = json.loads(response.content)
    #Перетворюе байти у текст
    print(json.dumps(data_dict, indent= 4))