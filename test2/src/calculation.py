# calculation.py
import os

from difflib import restore


def addition(num1: int, num2: int) -> int:
    return num1 + num2

def subtraction(num1: int, num2: int) -> int:
    return num1 - num2

def division(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ZeroDivisionError()
    return num1 / num2

class Cal():
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            f.write('test')
