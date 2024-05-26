# Создание пустого множества
my_set = set()  # написать my_set = {} нельзя, так как это будет пустой список
print(my_set)
# Создание множества с начальными значениями 
my_set_1 = {1, 2, 3}
print(my_set_1)
# Добавление элементов в множество
my_set.add(1)
my_set.add(2)
print(my_set)
# Удалить элемент из множества 
my_set.remove(1) # выдаст ошибку если захотим удалить элемент которого в множестве нет
my_set.discard(2) # не выдаст подобную ошибку 
print(my_set)
# Добавить в множество 100 элементов 
for i in range(0, 101):
    my_set.add(i)
# Очистить множество 
my_set.clear()
print(my_set)
# Обратиться к элементу множества 
print(my_set[0]) # - нельзя 
# Добавить в множество изменяемый тип данных 
my_set.add([1,2,3]) # - нельзя 

set_1 = {1,2,3}
set_2 = {2,3,4}
# Пересечение - операция на нахождение общих элементов - два способа 
print(set_1 & set_2)
print(set_1.intersection(set_2))
# Объединение -  операция сложения всех элементов двух множеств - два способа 
print(set_1 | set_2)
print(set_1.union(set_2))
# Вычитание -  поиск уникальных элементов одного множества (которых нет в другом)
# Два способа (важно какое множество вычитаем из какого):
print(set_1 - set_2)
print(set_2.difference(set_1))

# Дополнение update - применяем операцию непосредственно к текущему множеству
set_1.difference_update(set_2)
set_1.intersection_update(set_2)
print(set_1)
# Метод update - если хотим применить объединение непосредственно к текущему множеству
set_1.update(set_2)
print(set_1)

# Вывести уникальные элементы списка 1 раз 
my_list = [1,1,1,2,2,2,3,4,5,5]
print(set(my_list))
for i in set(my_list):
    print(i)
# Проверить является ли строка подмножеством другой строки? - метод .issubset()
str_1 = 'i l o v e c a t s'
str_2 = 'c a t s'
if set(str_2).issubset(str_1):
    print('ok')
# Проверить является ли строка cупермножеством другой строки? - метод .issuperset()
if set(str_1).issuperset(str_2):
    print('ok')
# Задача с Ваней и Петей
n = int(input()) # 10
result = set()
for i in range(1, n+1):
    result.add(i) # 1 2 3 4 5 6 7 8 9 10

while True:
    vanya = input() # 1 2 3 4 5
    if vanya == 'HELP':
        print(result)
        break
    else:
        vanya_set = set()
        vanya = vanya.split()
        for i in vanya:
            vanya_set.add(int(i)) # {1,2,3,4,5}
    answer = input()
    if answer == 'YES':
        result.intersection_update(vanya_set)
    else:
        result.difference_update(vanya_set)

    # 1 2 3 4 5 6 7 8 9 10 
    # 1 2 3 4 5 

    # 1 2 3 4 5 
    # 2 4 