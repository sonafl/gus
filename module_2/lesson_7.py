# Создание класса
class Car:
    mark = 'Volkswagen'
    model = 'Polo'
    color = 'white'
    speed = 0


# Создание экземпляра класса
my_car = Car()
print(my_car) # выведет информацию о классе объекта и где он находится в памяти компьютера 
print(type(my_car)) # к какому классу относится объект
# Обращение к свойствам класса
print(my_car.mark)
print(my_car.model)
print(my_car.color)
print(my_car.speed)
# Изменение свойства
my_car.color = 'black' # не действует на класс, меняется только для конкретного объекта
print(my_car.color)

# Создание второго экземпляра 
my_second_car = Car()
print(my_second_car.color) # свойство "цвет" не изменилось для всего класса, как и в новом объекте

# Создание класса спортивной машины 
class SportCar:
    # указываем названия атрибутов - начальные значения (пустая строка, ноль)
    mark = ''
    model = ''
    engine = 0
    speed = 0

# Создание 3 экземпляров класса
cars = []
for i in range(3):
    car = SportCar()
    # указываем конкретные значения свойств для каждого автомобиля 
    car.mark = input('Введите марку автомобиля ') 
    car.model = input('Введите модель автомобиля ')
    car.engine = int(input('Введите мощность двигателя '))
    car.speed = int(input('Введите максимальную скорость '))
    cars.append(car) # в списке будут находиться три объекта класса с информацией о классе и памяти в компьютере
print(cars)
for car in cars: 
    print(f'Марка автомобиля: {car.mark}')
    print(f'Модель автомобиля: {car.model}')
    print(f'Максимальная скорость автомобиля: {car.speed}')
    print(f'Мощность двигателя у автомобиля: {car.engine}')
