class Car:

    # магический метод __new__ - cоздает объект класса (через возвращение)
    # конструкция *args - условная конструкция кортежа, в который помещаются неименованные аргументы (т.е. свойства)
    # конструкция **kwargs - условная конструкция словаря, в который помещаются именованные аргументы (т.е. свойства)
    def __new__(cls, *args, **kwargs):
        # print('Работает метод __new__')
        # print(kwargs)
        # метод new должен вернуть объект и информацию о нем
        return super().__new__(cls)

    def __init__(self, model):
        self.model = model
        #self.mark = mark
        # self.color = color
    
    # магический метод str  - отображает информацию об объекте для пользователя 
    def __str__(self):
        return f'Объект относится к классу  Сar, модель машины - {self.model}'
        
    # магический метод repr
    def __repr__(self): # отображает информацию об объекте для разработчика
        return f'Сar({self.model})'
    
# my_car = Car('Veyron', 'Bugatti', 'orange') - пример неименнованных аргументов, здесь нужен args
# my_car = Car(model='Veyron', mark='Bugatti', color='orange') -  пример именнованных аргументов, здесь нужен kwargs
my_car = Car('Veyron')
# print(my_car)

# Шаблон проектирования SingleTon
class Captain:
    # создаем приватное свойство, в которое поместим информацию об объекте
    __cap = None

    def __new__(cls, *args, **kwargs):
        # если информации об объекте нет (то есть он еще не создан), то создаем первый и единственный объект
        if cls.__cap is None:
            #  помещаем в свойство информацию об объекте
            cls.__cap = super().__new__(cls)
        # возвращаем свойство, создавая объект класса
        return cls.__cap 

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

captain = Captain('Михаил', '34', '179', '87')
new_captain = Captain('Олег', '29', '179', '75')
# print(captain.__dict__)
# print(new_captain.__dict__)


# Задача с копилкой 
class MoneyBox:

    def __init__(self, money=0):
        self.__money = money

    def __repr__(self):
        return f'MoneyBox({self.__money})'
    
    def __add__(self, other):
        # isinstance - функция, проверяющая принадлежность к определенному типу данных (или к классу)
        if isinstance(other, (int, float)):
            # создаем новый объект со сложенным значением
            return MoneyBox(self.__money + other)
        else:
            print('Некорректное сложение')
    # зеркальный метод сложения, позволяющий менять местами операнды сложения (10+box)
    def __radd__(self, other):
        return self.__add__(other)

box = MoneyBox(40)
# box = box + 10
# box += '10'
box = 10 + box 
print(box)