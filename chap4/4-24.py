n = int(input())
k = 1
for i in range(n):
    for j in range(k):
        print(f'{j + 1}*{i + 1}={(i + 1) * (j + 1):<4}', end = '')
    print()
    k += 1