# https://yandex.ru/pogoda/
import requests
# метод get выполняет GET-запрос к странице на получение данных из нее
# response = requests.get('https://yandex.ru/pogoda/')
# атрибут text возвращает html-код страницы
# print(response.text)

# Подключение к API Яндекс Погоды
# ключ api - 90cb98b6-1a86-4bbb-b875-cde4399b7355
# Координаты Новосибирска: 55.0415, 82.9346
# Подключаем все параметры 
coords = (55.0415, 82.9346)
url = 'https://api.weather.yandex.ru/v2/forecast?'
headers = {'X-Yandex-API-Key' : '90cb98b6-1a86-4bbb-b875-cde4399b7355'}  # шапка подключения - ключик
params = {'lat' : coords[0], 'lon' : coords[1], 'lang' : 'ru_RU'} # подключение обязательных и необязательных полей в запросе
# Делаем запрос
response = requests.get(url, headers=headers, params=params)
# print(response)
# Преобразуем ответ в программную структуру
data = response.json()
# print(data)
fact = data['fact']
print(fact)
# Температура
print(f"Температура: {fact['temp']}")
# Как ощущается погода?
print(f"Ощущается как: {fact['feels_like']}")
# Cкорость ветра
print(f"Скорость ветра: {fact['wind_speed']}")
# Давление
print(f"Давление: {fact['pressure_mm']}")
# Направление ветра 
dir = {
    'nw' : 'северо-западное',
    'n' : 'северное', 
    'ne' : 'северо-восточное',
    'e' : 'восточное', 
    'se' : 'юго-восточное', 
    's' : 'южное', 
    'sw' : 'юго-западное', 
    'w' : 'западное',
    'c' : 'штиль'
}
print(f"Направление ветра: {dir[fact['wind_dir']]}")