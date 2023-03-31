from functools import reduce
from typing import List


class Calculator:
    @staticmethod
    def add(*args):
        res = 0
        for arg in args:
            res += arg
        return res

    @staticmethod
    def multiply(*args: List[int or float]):
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, b: a - b, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
