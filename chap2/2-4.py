a, n = input().split()
n = int(n)
s = sum([int(a * i) for i in range(1, n + 1)])

print(f"s = {s}")