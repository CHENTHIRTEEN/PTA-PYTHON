n = int(input())
f = []
m = []
peo = []
for i in range(n):
    temp = input().split()
    peo.append(temp[1])
    if temp[0] == '0':
        f.append(temp[1])
    else:
        m.append(temp[1])
for i in range(int(n/2)):
    if peo[i] in f:
        j = f.index(peo[i])
        print(peo[i] + ' ' + m[-j - 1])
    else:
        j = m.index(peo[i])
        print(m[j] + ' ' + f[-j - 1])