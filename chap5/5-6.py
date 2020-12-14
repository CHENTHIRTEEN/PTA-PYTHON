n = int(input())
num = list(input().split())
year = {}
for i in num:
    if i in year:
        year[i] += 1
    else:
        year[i] = 1
num1 = set(num)
num = [int(i) for i in num1]
num.sort()
for i in num:
    print(f'{i}:{year.get(str(i))}')