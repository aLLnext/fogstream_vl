'''Дана строка. Разрежьте ее на две равные части
(если длина строки — четная, а если длина строки нечетная,
то длина первой части должна быть на один символ больше).
переставьте эти две части местами, результат запишите в новую строку и выведите на экран.'''
str = open("input.txt", "r").read()
str1 = str[0:(len(str) + 1) // 2:1]
str2 = str[(len(str) + 1) // 2:len(str):1]
print(str2 + str1)