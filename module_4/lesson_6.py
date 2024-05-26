import requests
from datetime import datetime
key = '570406168ce74a28ad01ba52c83214db'
coords = (59.9386, 30.3141)
url = 'https://api.openweathermap.org/data/2.5/weather?'

params = {
    'lat' : coords[0], 
    'lon' : coords[1], 
    'appid' : key, 
    'utils' : 'metric', 
    'lang' : 'ru'
}

response = requests.get(url, params=params)
data = response.json()
#print(data)
# Температура
main = data['main']
print(f"Температура на данный момент - {main['temp']}")
# Как ощущается?
print(f"Как ощущается погода сейчас - {main['feels_like']}")
# Влажность
print(f"Влажность - {main['humidity']}")

# Описание погоды
weather = data['weather']
print(f"Какая погода сейчас: {weather[0]['description']}")
# Ветер
print(f"Сила ветра: {data['wind']['speed']}")
# Время заката и восхода
# Timestamp - это милисекунды для обозначения 
# datetime.fromtimestamp -  из таймстемпа сделать дату 
# strftime - отсеить дату и остатвить только ЧАСЫ МИНУТЫ И СЕКУНДЫ 
print(f"Время восхода: {datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')}")
print(f"Время заката: {datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')}")

      