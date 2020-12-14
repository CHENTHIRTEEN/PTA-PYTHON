import math
m, n = map(int, input().split())
flag = True
for i in range(m, n + 1):
    num = []
    num.append(1)
    for j in range(2, int(math.sqrt(i) + 1)): #int(math.sqrt(i) + 1)
        if i % j == 0:
            num.append(j)
            if j * j != i:
                num.append(i // j)
    if sum(num) == i:
        num.sort()
        print(f"{i} = {' + '.join(map(str, num))}")
        flag = False

if flag:
    print('None')