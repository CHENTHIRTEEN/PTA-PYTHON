n = int(input())
f1 = 1
f2 = 1

while f1 < n:
    f1, f2  = f1 + f2, f1
print(f1)
