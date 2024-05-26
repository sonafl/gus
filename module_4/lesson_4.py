from functools import wraps
def decorator(func):
    # Второй способ через декоратор wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + ' рублей.'
    # Первый вариант, который позволит получить из декоратора информацию об обертываемой функции cost
    # Утрачиваем уникальные значения функции-обертки wrapper
    #wrapper.__name__ = func.__name__
    #wrapper.__doc__ = func.__doc__
    return wrapper 

@decorator
def cost(price):
    """Эта функция возвращает стоимость товара"""
    return f'Стоимость товара: {price}'

# print(cost.__name__)
# print(cost.__doc__)

# Логирование
books = {}

def log_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Название вызываемой функции: {func.__name__}')
        print(f'Документация вызываемой функции: {func.__doc__}')
        return func(*args, **kwargs) 
    return wrapper

@log_info
def add_book(title, author):
    """Функция добавляет в каталог книги"""
    if title not in books:
        books[title] = author
        print('Книга добавилась в каталог успешно')
    else:
        print('Книга уже есть в словаре, она не была добавлена в каталог')

@log_info
def find_book(title):
    """Функция ищет книгу в каталоге по ее названию"""
    if title in books:
        print('Книга есть в каталоге')
    else:
        print('Книги в каталоге нет. Вы можете ее добавить')

#add_book('Властелин колец', 'Толкин')
#find_book('Герой нашего времени')

# Парк аттракционов 

def check_age(min_age):
    def decorator(func):
        def wrapper(age, *args, **kwargs):
            if age < min_age:
                return('Прохода нет')
            return func(age, *args, **kwargs)
        return wrapper
    return decorator

@check_age(18)
def go_to_atrr(age, attr):
    return f'Проход на аттракцион "{attr}" разрешен'

print(go_to_atrr(20, 'Американские горки'))

