m, n = map(int, input().split())

s = 0
k = 0
if m == 1:
    m = 2
for i in range(m, n + 1):
    isPrimer = True
    for j in range(2, i):
        if i % j == 0:
            isPrimer = False
            break
    if isPrimer:
        s += i
        k += 1
print(f'{k} {s}')