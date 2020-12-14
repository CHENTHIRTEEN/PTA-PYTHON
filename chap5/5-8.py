a, b = map(int, input().split())
k = 0
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        k += 1
print(k)