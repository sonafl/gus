# Создание списка списков 
data = [[1,2,3], [3,4,5], [5,6,7]]
data = [
     [1,2,3],
     [2,3,5], 
     [4,5,6]
 ]
# Индексация такого списка
print(data[0][1]) # двойная индексация 

# Итерирование вложенного списка
for i in data:
    for elem in i:
        print(elem) 
# Найти сумму чисел во вложенном списке - 2 способа
summa = 0
for i in data:
    for elem in i:
        summa += elem
print(summa)

summa = 0
for i in data:
    summa += sum(i)
print(summa)

# Вложенные списки и строки
## Задача про ЕГЭ 
data = []
n = int(input()) # 6
for i in range(n):
    student = input('Имя БАЛЛ1 БАЛЛ2 БАЛЛ3').split() # получаем из строки список с баллами 
    data.append(student)
print(data) # [['Петя', '45', '67', '78'], ['Иван', '69', '70', '84']]

pr_1 = 0
pr_2 = 0
pr_3 = 0
for i in data:
    # Сумма баллов 
    summa = int(i[1]) + int(i[2]) +int(i[3]) # обращаемся к каждому баллу ученика
    print(f'Cтудент {i[0]} в сумме получил {summa} баллов')
    pr_1 += int(i[1])
    pr_2 += int(i[2])
    pr_3 += int(i[3])

print(pr_1/n)
print(pr_2/n)
print(pr_3/n)

# Вложенные словари 
data = {
    'Петя': {'Матан': 80, 'РЯ': 95, 'Информатика': 78},
    'Паша': {'Матан': 80, 'Физика': 79},
    'Тимур': {'Информатика': 90, 'Биология': 90},
    'Никита': {'Биология': 80, 'Информатика': 78, 'Физика': 80, 'РЯ': 80}
}

# [('ключи', 'значение'), ('ключи', 'значение')] - dict.items()
# [значения, значения, значения] - dict.values()

# Сумма баллов для каждого ученика
for names, grades in data.items():
    print(names,sum(grades.values()))

# Средний балл по каждому предмету 
scores = {} # {'Матан': [80, 80], 'Информатика':[90, 78, 78]}

for grades in data.values():
    for subjects in grades.keys():
        if subjects not in scores:
            scores[subjects] = [grades[subjects]] 
            # создаем новую пару ключ-значение, где ключ - название предмета, 
            ## а значение - первый балл за этот предмет в виде списка
        else:
            scores[subjects].append(grades[subjects]) # обновляем значение ключа, добавляя в список новый балл

for subject, grade in scores.items():
    print(subject, sum(grade)/len(grade))
