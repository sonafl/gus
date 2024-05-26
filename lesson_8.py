class Car:
    # __init__ - инициализатор объектов класса, он срабатывает сразу же при создании объекта
    def __init__(self, mark, model, color, speed=200):
        # указывать свойства для каждого объекта (они будут общими для всех, но при этом принадлежать объекту)
        self.mark = mark
        self.model = model
        self.color = color
        self.speed = speed

    # создает новое локальное (принадлежащее только объекту) свойство
    # self - параметр, ссылка на объект класса (как счетчик i в цикле for i in list - ссылка на элемент списка)
    def set_engine(self, power_engine):
        # print('Двигатель и программа успешно работают')
        self.power_engine = power_engine
    
    # выводит все свойства объекта
    def show_info(self):
        print(f'Марка автомобиля {self.mark}')
        print(f'Модель автомобиля {self.model}')
        print(f'Цвет автомобиля {self.color}')
        print(f'Скорость автомобиля {self.speed}')
    
    # возвращает все свойства объекта, чтобы их сохранить 
    def get_params(self):
        return self.mark, self.model, self.color, self.speed
    
    def __del__(self):
        print('Сработал метод удаления')

car_1 = Car('Nissan', 'Tiana', 'black')
car_2 = Car('Bugatti', 'Veyron', 'blue', 700)

print(car_1.speed)
Car.set_engine(car_1)
car_1.set_engine(350)
print(car_1.power_engine)

# __dict__ - магический метод, выводит все локальные свойства объекта или общие данные о классе
print(car_1.__dict__)
print(car_2.__dict__)
print(Car.__dict__)

car_1.show_info()

all_params = car_1.get_params()
print(all_params )