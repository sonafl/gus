# Создание словаря 
english_dict = {
    'cat' : 'кот',
    'apple' : 'яблоко',
    'house' : 'дом'
}

# Какие типы данных каким образом используются в словарях? 
# Ключом словаря могут быть ТОЛЬКО неизменяемые типы: строка, целые числа и вещественные числа
# Значением может быть ВСË ЧТО УГОДНО

# Обращение к элементу словаря 
print(english_dict['cat'])

key = input()
print(english_dict[key])
# Проверка наличия ключа в словаре и вывод его значения 
if key in english_dict:
    print(english_dict[key])
else:
    print('Такого ключа не существует')
# Метод get - выводит значение по ключу, если ключа нет вывведет дефолтное значение (через запятую указано)
print(english_dict.get(key, 'Такого ключа нет'))


# Добавление элементов в словарь 
english_dict['blue'] = 'cиний'

# Обновление элементов в словаре
english_dict.update({'blue' : 'грустный'})
#  если указать несуществующйи ключ - добавит новую пару 
english_dict.update({'зеркало' : 'mirror'})
# Удаление элемента из словаря: 3 способа:
del english_dict['зеркало']
# pop удалит ключ и значение, а значение вернет - его можно сохранить в переменную 
a = english_dict.pop('зеркало')
# popitem  -  удалит последнюю пару, но ключ и значени вернет - их можно сохранить в переменную или вывести 
print(english_dict.popitem())


# Что будет, если добавить одинаковые ключи?
# english_dict['thing'] = 'вещь'
# english_dict['thing'] = 'обстоятельство'
# english_dict['thing'] = 'ситуация'
# print(english_dict)

# Функции и методы 

print(len(english_dict)) # количество элементов 
print(english_dict.keys()) # список из всех ключей 
print(english_dict.values()) # список из всех значений 
print(english_dict.items()) # список из значений и ключей в виде списка с кортежами - развернутый словарь по сути

# Переделать в словарь из items
# dict_1 = english_dict.items()
# print(dict(dict_1))

dict_new = english_dict.copy() # дубликат словаря 
english_dict.clear() # очистка словаря 
print(english_dict)


# Задача про книги
books = {}
while True:
    print('1. Добавить книгу')
    print('2. Удалить книгу')
    print('3. Вывести автора книги')
    print('4. Вывести все книги')
    print('0. Завершить работу с каталогом')
    # запрашиваем у пользователя номер действия
    user_command = input('Введите номер действия ')
    # проверка, что пользователь выбрал 0
    if user_command == '0':
        print('пока')
        break
    # проверка, что пользователь выбрал 1
    elif user_command == '1':
        title = input('Введите название книги')
        while title in books:
            title = input('Введите еще раз: ')
        author = input('Введите автора ')
        books[title] = author
    # проверка, что пользователь выбрал 2
    elif user_command == '2':
        title = input('Введите название книги')
        if title in books:
            del books[title]
        else:
            print('Такой книги нет')
    # проверка, что пользователь выбрал 3
    elif user_command == '3':
        title = input('Введите название книги')
        print(books.get(title, 'Такой книги нет'))
    # проверка, что пользователь выбрал 4
    elif user_command == '4':
        # когда используем for для  словаря, keys -  это ключи на каждой итерации, books[keys] - их значения 
        for keys in books:
            print(f'Название - {keys}, автор - {books[keys]}')
    # проверка, что пользователь выбрал некорректное действие
    else:
        print('Введите действие заново')
