'''Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.'''
arr = list(open("input.txt", "r").read().split())
for index in range(len(arr) - 1):
    if arr[index] < arr[index + 1]:
        print(arr[index + 1])