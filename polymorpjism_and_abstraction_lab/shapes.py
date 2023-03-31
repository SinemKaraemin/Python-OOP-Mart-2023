import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * self.__radius * math.pi

    def calculate_area(self):
        return math.pi * self.__radius ** 2


class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def calculate_area(self):
        return self.__width * self.__height


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
