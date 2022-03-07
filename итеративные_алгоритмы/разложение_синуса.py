# sin x => ((-1) ** (n-1) * x ** (2n-1)) /(2n-1)!
import math
from itertools import count

EPSILON = 0.000000000000001  # до какой точности считаем (точность подсчета)


# поиск элемента бесконечного ряда



def get_sin_x(x):
    """ итеративный алгоритм вычисления sin x"""

    def get_item_n(n):
        """замыкаем функцию"""
        return ((-1) ** (n - 1) * x ** (2 * n - 1)) / math.factorial(2 * n - 1)
    sum_ = 0
    for i in count(1, 1):
        current_item = get_item_n(i)
        sum_ += current_item
        if abs(current_item) <= EPSILON:
            sum_ += current_item
            return sum_


value_for_sinus = 45 * math.pi / 180  # -1 до 1

print(math.sin(value_for_sinus))  # через встроенную библиотеку
print(get_sin_x(value_for_sinus))  # через нашу формулу. Через формулу Тейлора
