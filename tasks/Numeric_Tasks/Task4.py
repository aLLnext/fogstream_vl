P, X, Y, *arr = map(int, open("input.txt", "r").read().split())
X = X + Y / 100
X += X * (P / 100)
print("%.2f" % (X))