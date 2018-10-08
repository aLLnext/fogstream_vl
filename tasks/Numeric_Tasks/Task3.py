LESSON_DURATION = 45
n, *arr = map(int, open("input.txt", "r").read().split())
time = LESSON_DURATION * n
for lesson in range(n - 1):
    if lesson % 2:
        time += 15
    else:
        time += 5
hour = time // 60
minute = time - hour * 60
print("LESSON ENDS:", (9 + hour) % 24,':',minute)