n, *arr = map(int, open("input.txt", "r").read().split())
hour = n // 60
minute = n - hour * 60
print("TIME: ", hour % 24, ':', minute)
