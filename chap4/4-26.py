n = int(input())
sum = 1
temp = 1
if n == 1:
    print('n=1,s=1')
    exit(0)
for i in range(3, n + 1, 2):
    temp = temp * i * (i - 1)
    sum += temp
print(f'n={n},s={sum}')