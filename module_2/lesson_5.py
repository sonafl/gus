# Существует список со строками, которые представляют собой числа.
# Необходимо вывести максимальное из них. 
str_nums = ['23', '8', '44', '7']
print(max(str_nums, key=int)) # параметр key принимает функцию

# В программе хранится список со строками различной длины
# Необходимо вывести из списка строку с максимальной длиной

words = ['восемнадцать', 'четыре', 'пять']
max_word = ''
for i in words:
    if len(i) > len(max_word):
        max_word = i
print(max_word)
print(max(words, key=len)) 

# Создайте функцию, которая умножит число на 2
def double(x):
    return x*2
number = double(8)
print(number)

# анонимная функция:
# lambda <аргумент>: <действие>
number = lambda x: x*2
print(number(8))

# условный оператор внутри анонимной функции
numbers = lambda x: 'ok' if x % 2 == 0 else 'ne_ok'
print(numbers(5))

# Есть список с числами, выведите число, у которого самый большой квадрат. 
numbers = [3,4,5,7,8,10]
print(max(numbers, key=lambda x: x**2)) # анонимные функции часто используются внутри других функций

# сортировка словаря 
numbers = {(1,2,3) : 5, (4,5,6) : 3, (6,7,8) : 8}
# dict_items([((1, 2, 3), 5), ((4, 5, 6), 3), ((6, 7, 8), 8)])
numbers = sorted(numbers.items(), key=lambda x: x[1]) # сортировка по значению словаря
print(dict(numbers))

# Функция map - преобразование, сопоставление
# list(map(<функция>, <к кому применяем, например, список>))

# Список из строк превратить в список чисел
str_nums = ['23', '8', '44', '7']
new_num = [int(num) for num in str_nums]
print(new_num)
new_num = list(map(int, str_nums))
print(new_num)
str_numbers = list(map(str, new_num))
print(str_numbers)

# Ввод списка целых чисел
nums = list(map(int,input().split()))
print(nums)


# Задача со степенями
base = [1,2,3,4] # основание степени
exp = [3,4,5,6] # показатель степени
new = list(map(lambda x,y: x**y, base, exp))
print(new)


# Функция filter - отобрать определенные элементы
# list(filter(<функция с выражением истинно/ложно>, <к кому применяем, например, список>))

# Есть список со словами разной длины. Нужно создать новый список,
## в котором будут только слова, состоящие из 5 и более букв
words = ['котик', 'дом', 'лилия', 'школа', 'буй']
new_words = list(filter(lambda x: len(x) >= 5, words))
print(new_words)

# Палиндромы 
words = ['анна', 'оно', 'sos', 'котик', 'дом']
new_words = list(filter(lambda x: x == x[::-1], words))
print(new_words)

# Функция reduce - сокращение действий за счет накопления 

# Найдите произведение чисел в списке. 
from functools import reduce
numbers = [1,2,3,4,5]
pr = reduce(lambda x, y: x*y, numbers)
print(pr)

