# class Rectangle:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
    
#     def get_area(self):
#         return self._length * self._width

# class Triangle:
#     def __init__(self, base, height):
#         self._base = base
#         self._height = height
    
#     def get_area(self):
#         return 0.5 * self._base * self._height

# импортируем модуль Фмгуры
from figure import Figure

class Rectangle(Figure):
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def get_area(self):
        return self._length * self._width
    
    def get_perimeter(self):
        return (self._length + self._width) * 2

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    
    def get_area(self):
        p = (self._side1 + self._side2 + self._side3) / 2  
        return (p * (p - self._side1) * (p - self._side2) * (p - self._side3))**0.5
    
    def get_perimeter(self):
        return self._side1 + self._side2 + self._side3
    
rect1 = Rectangle(5,6)
rect2 = Rectangle(14, 30)
tri1 = Triangle(4, 5, 6)
tri2 = Triangle(7, 8, 7)

figs = [rect1, rect2, tri1, tri2]

for i in figs:
    print(f'Площадь фигуры равна {round(i.get_area(),2)}')
    print(f'Периметр фигуры равен {i.get_perimeter()}')

class Circle(Figure):
    def __init__(self, radius):
        self._raduis = radius
    
circle = Circle(5)
area = circle.get_area()
perimeter = circle.get_perimeter()















# Формула Герона
# def get_area(self):
#     p = (self._side1 + self._side2 + self._side3) / 2  
#     return (p * (p - self._side1) * (p - self._side2) * (p - self._side3))**0.5