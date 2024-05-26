# Телеграм-бот III

'''
План урока:
1) Введение, повторение, разбор ДЗ (10 минут)
2) Оформление файла с погодными функциями (35 минут)
3) Перерыв (10 минут)
4) Телеграм-бот + погодные функции (40 минут)
5) Заключение (5 минут)
'''

# -----------------------------------------------------------------------------------------------------------

# Оформление файла с погодными функциями

'''
Первая часть занятия посвящена подготовке отдельного питоновского файла, внутри которого
будут содержаться функции для работы с погодными данными (в примере файл называется api.py) 
Ранее нам приходилось искать координаты населенного пункта для получения данных о погоде. 
OpenWeather API предоставляет свой инструмент - Geocoding API, который позволяет получить координаты указанного города.
https://openweathermap.org/current - документация для получения текущей погоды
https://openweathermap.org/api/geocoding-api - документация Geocoding API
'''

import requests
from datetime import datetime

API_KEY = 'dc610ddd2e0bfa14d7ae1e16c57b389e'

# функция для получения координат указанного города
def get_coords(city_name):
    url = 'http://api.openweathermap.org/geo/1.0/direct?'
    params = {
        'q': city_name,
        'appid': API_KEY
    }
    response = requests.get(url, params=params)
    # ответ приходит в виде списка с одним объектом - словарем, 
    # поэтому обращаемся по индексу, чтобы оставить только словарь
    data = response.json()[0]
    return data['lat'], data['lon']

'''
ВАЖНО: чтобы не писать с нуля функцию get_weather(), возьмите код с предыдущего занятия.
Предупредите учеников заранее, что им пригодится код с предыдущего урока.
'''

def get_forecast(city_name):
    coords = get_coords(city_name)
    url = 'https://api.openweathermap.org/data/2.5/forecast?l'
    params = {
        'lat': coords[0],
        'lon': coords[1],
        'appid': API_KEY, 
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    data = response.json()['list']
    forecast = {}
    for elem in data:
        date = datetime.fromtimestamp(elem['dt']).strftime('%d.%m.%Y')
        if date not in forecast:
            forecast[date] = {}
        time = datetime.fromtimestamp(elem['dt']).strftime('%H:%M')
        main = elem['main']
        description = elem['weather'][0]['description']
        wind = elem['wind']
        forecast[date][time] = (f"Температура {main['temp']} °C, {description}",
            f"Ощущается как {main['feels_like']} °C",
            f"Влажность {main['humidity']} %",
            f"Ветер {wind['speed']} м/c")
    return forecast

# print(get_forecast('Москва'))

# функция для получения погоды в указанном городе
def get_weather(city_name):
    # вызываем функцию get_coords() для получения координат города
    coords = get_coords(city_name)
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {
        'lat': coords[0],
        'lon': coords[1],
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    data = response.json()
    main = data['main']
    description = data['weather'][0]['description']
    wind = data['wind']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    # возвращаем кортеж со строками
    return (f"Температура {main['temp']} °C, {description}",
            f"Ощущается как {main['feels_like']} °C",
            f"Влажность {main['humidity']} %",
            f"Ветер {wind['speed']} м/c",
            f"Восход в {datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')}",
            f"Закат в {datetime.fromtimestamp(sunset).strftime('%H:%M:%S')}")
# -----------------------------------------------------------------------------------------------------------

# Телеграм бот + погодные функции (40 минут)

'''
Вторая часть урока будет проходить в отдельном питоновском файле (в примере файл называется bot.py).
Создайте вместе с учениками в папке текущего проекта файл bot.py и продолжайте работу в нем.
'''

