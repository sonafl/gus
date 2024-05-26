import json 

# словарь является программной структурой
human = {
    'name' : 'Джек', 
    'age' : 18, 
    'city' : 'Москва'
}

# функция dumps - из программной структуры (словарь) создает json-строку
# ensure_ascii = False позволяет добавить в json-строку кириллицу 
human_json = json.dumps(human, ensure_ascii=False)
# print(human_json)

# функция dump - добавляет программную структуру в json-файл
# file = open('human.json', 'w', encoding='UTF-8')
# json.dump(human, file, ensure_ascii=False, indent=4)

# функция loads - из json-строки делает программную структуру (словарь)
human_dict = json.loads(human_json)
# print(type(human_dict))

# load - из json-файла извлекает данные и превращает в программную структуру (словарь)
file = open('human.json', encoding='UTF-8')
human_dict = json.load(file)
# print(type(human_dict))

file = open('example.json')
andrew_resume = json.load(file)
if andrew_resume['isFullTime'] == True and len(andrew_resume['languages']) >= 2:
    print('Проходит на 1 этап собеседования')
else:
    print('Не проходит на 1 этап')

