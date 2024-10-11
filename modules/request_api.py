import requests
#Імпортуваня бібліотеки Requests
from .read_json import read_json
#Імпортує із файла read_json функцію read_json
import json
#Імпортуваня json
data_api = read_json(name_file= 'config_api.json')
#
API_KEY = data_api['api_key']
#Змінна зі значенням api ключа
CITY_NAME = data_api['city_name']
#Змінна з ім'ям міста
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Посилання на погоду 
response = requests.get(URL)
#
if response.status_code == 200:
    #Умова яка перевіряє чи були отрімані данні
    data_dict = json.loads(response.content)
    #Зберігаемо данні о погоді (?)
    print(json.dumps(data_dict, indent= 4))