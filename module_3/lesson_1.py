# Класс Машина:
# цвет, скорость (защищенный), модель (приватный)
# метод show_info

class Car:
    def __init__(self, color, model, speed = 0):
        self.color = color
        self.__model = model
        self._speed = speed
    
    def show_info(self):
        print(f'Цвет машины: {self.color}')
        print(f'Модель машины: {self.__model}')
        print(f'Скорость машины: {self._speed}')
    
    # геттеры - это методы по безопасному получению значения в защищенном или приватном атрибуте
    def get_model(self):
        return self.__model
    
    def get_speed(self):
        return self._speed
    
    def set_speed(self, new_speed):
        if new_speed < 0:
            print('Скорость не может быть отрицательной')
        else:
            self._speed = new_speed

my_car = Car('red', 'Zhiguli', 140)
#my_car.show_info() - внутри класса можно обращаться к любым полям 
# print(my_car.color)
# print(my_car._speed) - обращаться к защищенными в Питоне можно 
# print(my_car.__model) - приводит к ошибке
# my_car._Car__model = 'Nissan Tiana' # обход системы - искажение имени поля - обращение и изменение поля 
# print(my_car._Car__model)
# print(my_car.get_model())
# print(my_car.get_speed())

my_car.set_speed(-130)
print(my_car.get_speed())