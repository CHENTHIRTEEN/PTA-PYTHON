m, n = map(int, input().split())
if m < n:
    m, n = n, m
for i in range(n, 0, -1):
    if m % i == 0 and n % i == 0:
        print(f'{i} ', end = '')
        break
for i in range(m, m * n + 1):
    if i % m == 0 and i % n == 0:
        print(i)
        break