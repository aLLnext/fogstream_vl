LENGTH_MKAD = 109
V, T, *arr = map(int, open("input.txt", "r").read().split())
S = (V * T) % LENGTH_MKAD
print(S)