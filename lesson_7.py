# Создание функции
# def - определяет функцию, указываем ее название, аргументы, которые ей нужны в работе
def show_info(lst):
    print(f'Максимальное число: {max(lst)}')
    print(f'Минимальное число: {min(lst)}')
    print(f'Среднее арифметическое: {sum(lst) / len(lst)}')
# Вводится последовательность чисел, пока не введется отрицательное число. 
## Необходимо найти максимальное, минимальное число, а также среднее в последовательности
numbers = []
n = int(input())
while n >= 0:
    numbers.append(n)
    n = int(input())
numbers_2 = [1,2,3,4,5]

# вызов функции
show_info(numbers)
show_info(numbers_2)

#Найти сумму всех цифр в числе 
def sum_digits(n):
    s = 0 
    while n > 0:
        s+= n % 10
        n = n // 10
    return s # return возвращает сам РЕЗУЛЬТАТ РАБОТЫ функции, а не ее вывод
num = 123

# Сохраним поличившееся значение функции и выведем его
summa = sum_digits(num)
print(summa)
print(sum_digits(num))



# Функция без аргументов 
def say_hello():
    print('Привет!')

say_hello()

# Функция для расчета площади окружности 
def circle_square(r):
    pi = 3.14
    return pi*r**2
radius = 10
print(circle_square(10))

# Рекурсия 
def F(n):
    if n == 1:
        return 1
    return 10 - F(n-1)
print(F(324))

# Библиотека math 
import math  # импортируем саму библиотеку
print(math.sqrt(100))

# импортируем все методы/функции библиотеки
from math import *
print(sqrt(100))

# Вывести список всех методов библиотеки 
print(dir(math))


# Библиотека random 
# подключаем отдельную функцию из random
from random import randint
print(randint(4, 100))