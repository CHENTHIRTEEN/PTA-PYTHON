num = list(map(int, input().split(',')))
target = int(input())
d = {}
for i in num:
    d[i] = target - i
for key, value in d.items():
    if key in num and value in num:
        print(num.index(key), num.index(value))
        break
else:
    print('no answer')