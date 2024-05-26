# условный оператор состоит из 3 блоков: if, elif, else
## существует иеархия: сначала идет if (главное условие), затем  elif (доп условие) и else (иначе)
### if и else в каждом условном операторе одни, elif - в любом количестве
#### условный оператор может быть создан одним только if, else и elif опционально

n = int(input())

if n < 0:
     print('Число отрицательное')
elif n == 0:
     print('Число является нулем')
else:
    print('Число положительное')

login = input()
password = input()
correct_login = 'maximum_student'
correct_password = '123'

# существуют сложные условия: их регулируют с помощью логических операторов: or - хотя бы одно условие должно выполнять, 
## and - все условия должны выполняться 
if login != correct_login or password != correct_password:
    print('Данные неверные')
else:
    print('Вход разрешен')

if login != correct_login and password != correct_password:
     print('Ни одни данные неверны')
elif password != correct_password:
    print('Неверный пароль')
elif login != correct_login:
    print('Неверный логин')
else:
    print('Вход разрешен')

# доработка калькулятора
num_1 = input()
num_2 = input()
operation = input('Введите +, -, *, **, / ')

# ставим главное условие: то, что ввел пользователь, является числом?
## для этого используем функцию .isnumeric()
if num_1.isnumeric() and num_2.isnumeric():
    num_1 = int(num_1)
    num_2 = int(num_2)
    # создаем вложенный условный оператор: который заработает в том случае, если выполняется главное условие (первый if)
    if operation == '+':
        summ = num_1 + num_2
        print('Сумма чисел равна: ' + str(summ))
    elif operation == '-':
        diff = num_1 - num_2
        print('Разность чисел равна: ' + str(diff))
    elif operation == '*':
        pr = num_1 * num_2
        print('Произведение чисел равно: ' + str(pr))
    elif operaration == '**':
        step = num_2 ** 2
        print('Квадрат числа равен: ' + str(step))
    elif operation == '/':
        del_1 = num_1 / num_2
        print('Частное чисел равно: ' + str(del_1))
    else:
        print('Неверная операция')
else:
    print('Неверный формат для математических вычислений')

# функции max и min, которые выводят максимальное или минимальное число из набора чисел 
print(max(134, 100, 200, 35))
print(min(134, 100, 200, 35))
