# функция декоратор - добавляет новый функционал в функцию, не меняя ее поведения
def decorator(func):
    # функция обертки - вызывается и добавляет доп действие 
    def wrapper():
        print('Начало работы')
        func()
        print('Конец работы')
    return wrapper
# Второй и более популярный способ вызова декоратора - вызывается одновременно с вызовомо основной функции 
@decorator
def hello():
    print('Привет!')

# hello()

# Первый способ вызова декоратора
# hello_message = decorator(hello)
# hello_message()

from time import time, sleep

def decorator(func):
    def wrapper():
        # засекает реальное время
        start_time = time()
        func()
        end_time = time()
        print(f'Время разморозки курицы: {end_time - start_time}')
    return wrapper

@decorator
def unfreeze():
    # функция, которая заставляет заснуть программу на некоторое количество секунд
    sleep(10)

# unfreeze()

#  Функция repeat - декоратор, который повторит работу другой функции 10 раз
# Для повтора используем for i in range()
# Функция message, выводит "привет!" и должна быть обернута

# def repeat(func):
#     def wrapper():
#         for i in range(10):
#             func()
#     return wrapper 

# @repeat
# def message():
#     print('Привет!')

# message()

def repeat(func):
    def wrapper(*args, **kwargs):
        for i in range(10):
            func(*args, **kwargs)
    return wrapper 

@repeat
def message(name):
    print(f'Привет, {name}!')

# message('Ваня')

def decorator(func):
    def access(*args, **kwargs):
        if kwargs.get('password') == '12345qwerty':
            print('Доступ разрешен')
            func(*args, **kwargs)
        else:
            print('Доступ к сообщению не разрешен')
    return access


@decorator
def send_message(message, password):
    print(f'Важное сообщение: {message}')

# user_password = input()
# message = 'Вы прелестные!'
 
# send_message(message, password=user_password)

def up(func):
    def wrapper(*args, **kwars):
        message = func(*args, **kwars)
        return message.upper()
    return wrapper

def warning(func):
    def wrapper(*args, **kwargs):
        return f'Вам пришло сообщение: {func(*args, **kwargs)}'
    return wrapper

# последовательность работы - снизу вверх. сначала сработает декоратор up, затем warning
@warning
@up
def send_message(message):
    return message

message_1 = send_message('У меня сегодня день Рождения!')
print(message_1)