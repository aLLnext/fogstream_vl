'''Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.'''
arr = list(map(int, open("input.txt", "r").read().split()))
for index in range(len(arr) - 1):
    if arr[index] * arr[index + 1] > 0:
        print(arr[index], arr[index + 1])
    elif arr[index] == 0 and arr[index + 1] == 0:
        print(arr[index], arr[index + 1])
