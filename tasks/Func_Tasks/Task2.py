'''Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
и возвращающую True, если оно простое, и False - иначе.'''
from math import sqrt


def is_prime(x):
    if x > 2 and x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x) + 2), 2):
        if x == i: continue
        if x % i == 0:
            return False
    return True


number = int(open("input.txt", "r").read())
print(is_prime(number))