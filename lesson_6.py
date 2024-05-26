# Деление на ноль (условный оператор)
n = int(input())
m = int(input())
if m == 0:
    print('ошибка')
else:
    print(n / m)

# Деление на ноль (конструкция try-except)
try:
    n = int(input())
    m = int(input())
    result = n / m
except ZeroDivisionError:
    print('Возникла ошибка! Делить на ноль нельзя!')
except ValueError:
    print('Возникла ошибка: введены неправильные значения!')
else:
    print(result)

# try - except - else
# try - блок кода, который нужно проверить на наличие ошибок
# except - блок кода, который работает, если возникла ошибка (их может несколько)
# else - блок кода, который работает, если ни одной ошибки не возникло. 
# finally - блок кода, который работает в любом случае, даже если возникла ошибка 

# Второй шанс
try:
    n = int(input())
    m = int(input())
    result = n % m 
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
    m = int(input('Введите заново число (не ноль)'))
except ValueError:
    print('Введены некорректные значения для перевода в int')
    n = int(input())
    m = int(input())
finally:
    result = n % m 
    print('Остаток от деления равен', result)

#  Лог - текстовый файл, где фиксируются ошибки. 
# Лог калькулятора.
name = input('Укажите свое имя:')
# открытие файла в режиме добавления
file = open('log_calc.txt', 'a', encoding='utf-8')
# запись в лог-файл введенного имени пользователя
file.write(f'Пользователь: {name}\n')

# цикл работы с калькулятором
while True:
    # ввод данных пользователем и вычисление результата
    try:
        # ввод двух чисел и знака операции
        num_1 = int(input('Введите первое число:'))
        oper = input('Введите операцию (+ - * / ** // %):')
        num_2 = int(input('Введите второе число:'))
        # запись в лог-файл о числах и операции
        file.write(f'Cовершается операция: {num_1}{oper}{num_2}\n')
        # вычисление результата
        result = eval(f'{num_1}{oper}{num_2}')
    # обработка ошибки деления на ноль
    except ZeroDivisionError:
        # повторный ввод второго числа
        num_2 = int(input('Делить на ноль нельзя, введите новое число:'))
        # запись информации в лог-файл
        file.write(f'Ошибка деления на ноль\n')
        file.write(f'Введено новое число: {num_2}\n')
    # обработка некорректного ввода чисел
    except ValueError:
        print('Введено некорректное значение!')
        # повторный ввод обоих чисел
        num_1 = int(input('Введите первое число:'))
        num_2 = int(input('Введите второе число:'))
        # запись информации в лог-файл
        file.write('Ввод некорректных значений\n')
        file.write(f'Введены новые числа: {num_1} и {num_2}\n')
    # обработка некорректного ввода операции
    except SyntaxError:
        # повторный ввод операции
        oper = input('Ошибка! Введите корректную операцию (+ - * / ** // %):')
        # запись информации в лог-файл
        file.write('Ввод некорректной информации\n')
        file.write(f'Введена новая информация: {oper}\n')
    # финальное вычисление результата и запрос новых данных от пользователя
    finally:
        # вычисление результат
        result = eval(f'{num_1}{oper}{num_2}')
        print(f'Результат операции: {num_1}{oper}{num_2} = {result}')
        # запись информации в лог-файл
        file.write(f'Результат: {num_1}{oper}{num_2} = {result} \n')
        # запрос пользователю на продолжение работы
        is_continue = input('Продолжить работу с калькулятором? (Y/N):')
        # если пользователь не хочет работать с калькулятором
        if is_continue == 'N':
            print('До свидания!')
            # закрываем файл и выходим из цикла
            file.write('----------------------------------------\n')
            file.close()
            break
        print('----------------------------------------')  