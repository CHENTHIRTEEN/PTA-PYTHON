n = int(input())
sum = 1
temp = 1
for i in range(1, n + 1):
    temp /= i
    sum += temp
print(f'{sum:.8f}')