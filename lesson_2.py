# Создание кортежа - два способа 
my_tuple = tuple()
my_tuple = ()
# Создание кортежа с начальными значениями
my_tuple = (1,2,3)
print(my_tuple)
# Конвертация списка в кортеж и наоборот 
my_tuple = tuple([1,2,3])
print(my_tuple)
my_list = list(my_tuple)
print(my_list)
# Индексация в кортеже
print(my_tuple[-1])
# Можно ли заменить элемент в кортеже?
my_list[0] = 5
print(my_list) # - со списком можно 
my_tuple[0] = 5 # - со кортежом нельзя
# Распаковка кортежа 
first, second, third = my_tuple
print(first, second, third)
# first, second = my_tuple
# first, second, third, last = my_tuple - эти строки приведут к ошибке
# сколько элементов в кортеже, столько и переменных 


# Итерирование по кортежу
for i in my_tuple:
    print(i)

# Метод .count()
my_tuple = (1,2,3,1)
print(my_tuple.count(1))
# Метод .index() - первхое вхождение элемента в кортеж/список 
print(my_tuple.index(2))
print(my_tuple.index(1))

# Остались sum(), max(), min(), len()

# Сложение кортежей
first = (1,2,3)
second = (4,5,6)
third = first + second
print(third)
third_1 = first[:2] + second[1:]
print(third_1)

# Кортежи и функции
def x(a,b,c):
    print(a,b,c)

objects = (1,2,3)
x(*objects) # вводим аргументы для функции в виде распакованного кортежа
# звездочка распакует кортеж и выведет элементы в 1 строчку через пробел
print(*objects)

def new(a,b,c):
    summ = a + b + c
    diff = a - b - c
    return summ, diff # return нескольких значений возвращает их в виде кортежа
print(new(*objects))
summ, diff = new(*objects)
print(summ)
print(diff)

# Практические кейсы:
# Условный оператор: есть ли что-то в кортеже или нет? 
empty = ()
if empty:
    print('Непустой')
else:
    print('Пустой')
new = (1,) # -  создание кортежа с 1 элементом
if new:
    print('Непустой')
else:
    print('Пустой')


# Вложенный список
my_tuple = ([1,2,3], [4,5,6])
my_tuple[0].append(4) # вложенный список в кортеж можно изменять
my_tuple[0].remove(4)
print(my_tuple)

# Изменение вложенного списка сохраняется в самом кортеже и в отдельной переменной
first = my_tuple[0]
for i in range(11):
    first.append(i)
print(first)
print(my_tuple[0])

my_tuple[0].append(4)
print(my_tuple[0])
print(first)

# Отличие от списков: библоиотек sys, функциях getsizeof
from sys import getsizeof

objects = []
# print(getsizeof(objects))

objects_tuple = ()
# print(getsizeof(objects_tuple))

for i in range(1000000):
    objects.append(i)
print(getsizeof(objects))
print(getsizeof(tuple(objects)))