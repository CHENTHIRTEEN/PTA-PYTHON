n = int(input())
sum = 0
f1 = 1
f2 = 2

for i in range(0, n):
    sum += f2 / f1
    f1, f2 = f2, f1 + f2

print(f'{sum:.2f}')