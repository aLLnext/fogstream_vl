H, M, S, *arr = map(int, open("input.txt", "r").read().split())
H %= 12
angleH = 360 / 12
angleM = angleH / 60
angleS = angleM / 60
angle = angleH * H + angleM * M + angleS * S
print(angle)