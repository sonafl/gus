# Открытие файла
file = open('file.txt')
print(file) # выведем общую информацию о файле
# Три способа прочитать содержимое файла:
## Метод read
data = file.read() #выведет ВСЕ из файла
print(data)
## Метод readline
data = file.readline() # выведет первую строку
print(data)
## Метод readlines
data = file.readlines() # выведет список со значениями из файла
print(data)
print('1\n', '2') # \n - служебный управляющий символ перехода на новую строку
# Закрытие файла
file.close()


# Чтение текстовой информации на латыни
file = open('file.txt')

# Чтение текстовой информации на кириллице
file = open('file.txt', encoding = 'UTF-8') 
# указываем кодировку каждый раз, когда имеем дело с кириллицей
print(file.read())

# Итерирование по файлу 
for line in file:
    print(line.strip('\n')) # избавляемся от \n

# Найти сумму всех чисел в файле
s = 0
for number in file:
    s += int(number)
print(s)

# Второй способ решения задачи: через список 
numbers = [] #list()
for number in file:
    numbers.append(int(number))
print(sum(numbers))

# Режим записи в файл - полностью перезаписать файл
file = open('file.txt', 'w') #  mode='w'
file.write('Привет, меня зовут Файл')

# Режим редактирования  - отредактировать файл, добавить в конец
file = open('file.txt', 'a')
file.write('\nКак у тебя дела?\n')

# Записать в файл числа от 1 до 20 
file = open('numbers.txt', 'w')
for i in range(1, 21):
    file.write(f'{i}\n')
file.close()

# Генерируем случайное число от 1 до 10. Например, 8. 
## Значит, 8 рандомных чисел от 1 до 100 нужно записать в файл
### Затем считать эти числа из файла и найти их произведение
from random import randint
n = randint(1, 10) #8
file = open('file_1.txt', 'w')
for i in range(n):
    random_num = randint(1, 100)
    file.write(f'{random_num}\n')
file.close()
file = open('file_1.txt')
p = 1
for num in file:
    p *= int(num)
print(p)

# Совместный режим чтение + запись. Метод seek
n = randint(1, 10)
file = open('file_1.txt', 'w+')
for i in range(n):
    random_num = randint(1, 100)
    file.write(f'{random_num}\n')
file.seek(0) # возвращает курсор в начало
p = 1
for num in file:
    p *= int(num)
print(p)

# Самостотятельное задание: 
# Записать в файл 10 рандомных чисел от 1 до 100
# Найти разницу между максимальным и минимальным числом в получившейся последовательности
# Что потребуется?