'''Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2),
вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.'''
from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1, y1, x2, y2 = map(float, open("input.txt", "r").read().split())

S = distance(x1, y1, x2, y2)
print(S)