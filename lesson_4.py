# Создайте новый список, в котором будут находиться квадраты чисел от 1 до N включительно. 
## N вводится с клавиатуры.

n = int(input())
numbers = [num**2 for num in range(1, n+1)]

numbers = [num**2 for num in range(1, int(input())+1)] # ввод числа можно добавить в генератор
print(numbers)


# Вводится строка с символами. Создайте список, элементами которого являются символы. 
# питон - п,и,т,о,н

word = input()
symbols = [sym for sym in word] # отсматриваем каждый символ в строке, добавляем в новый список
print(symbols)

symbols = [sym for sym in input()] # ввод строки можно добавить в генератор
print(symbols)


# Рассматриваются числа в диапазоне от 100 до 1000. 
## В список нужно добавить только числа кратные 7
numbers = [i for i in range(100, 1001) if i % 7 == 0] # условие в генераторе добавляется в конце

# Cамостоятельное решение. 
## Имеется список cities  c городами, нужно создать новый список только с теми городами,
## которые начинаются на А и имеют более 7 букв

cities = ['Архангельск', 'Армавир', 'Москва']
new = [ i for i in cities if i[0] == 'А' and len(i) >= 7] 

# Имеется список cities  c городами, 
# нужно создать новый список только с теми городами,
## в которых буквы встречаются один раз. Без учета регистра. 

new_cities = [i for i in cities if len(i.lower()) == len(set(i.lower()))] # set('мама') - {'м', 'а'}

# Генераторы словарей

# Есть словарь,  котором ключи - имена товаров, а значения - их цена.
## Создайте новый словарь, где цены будут увеличены на 20% 

fruits = {
    'малина' : 400,
    'яблоко' : 200,
    'мандарины' : 400
}

# указываем элемент словаря, то есть каждую пару ключ:значение
new_fruits = {key:value * 1.2 for key, value in fruits.items()}

# Генерация вложенных словарей и списков 

# Таблица умножения

# Классический метод:
n = int(input()) # 3
table = []
for i in range(1, n+1): # 1 2 3
    list_1 = []
    for j in range(1, n+1): # умножение каждого числа (1,2,3) на числа (1,2,3)
        # наполнение внутренного списка умножениями
        list_1.append(i*j) 
    table.append(list_1)
print(table)

# Через генерацию 
n = int(input())
# вложенная генрация: создаем вложенные списки
table = [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

# Числа и их делители

# Создание функции 
def get_divisors(num):
    divisors = []
    for i in range(2, num//2+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

# Генерация 
n = int(input()) # 3
m = int(input()) # 6
from time import time
start = time()
numbers = {i:get_divisors(i) for i in range(n, m+1) if len(get_divisors(i)) > 0}
stop = time()
print(stop-start) # 400/900 - 0.05

# Классический способ 

start = time()
numbers = {}
for i in range(n, m+1):
    divisors = get_divisors(i)
    if len(divisors) > 0:
        numbers[i] = divisors
stop = time()
print(stop-start) # 400/900 - 0.03
