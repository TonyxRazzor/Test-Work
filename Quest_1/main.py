import math


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(
            p * (p - self.side1) * (p - self.side2) * (p - self.side3)
            )

    def is_right_angled(self):
        return (self.side1 ** 2 + self.side2 ** 2 == self.side3 ** 2) or \
               (self.side1 ** 2 + self.side3 ** 2 == self.side2 ** 2) or \
               (self.side2 ** 2 + self.side3 ** 2 == self.side1 ** 2)


# Пример использования:

circle = Circle(5)
print("Площадь круга:", circle.get_area())

triangle = Triangle(3, 4, 5)
print("Площадь треугольника:", triangle.get_area())
print("Треугольник прямоугольный?", triangle.is_right_angled())
