def isNarcissus(n):
    sum = 0
    temp = n
    while temp != 0:
        sum += (temp % 10) ** len(str(n))
        temp = temp // 10
    if sum == n:
        print(n)

n = int(input())
for i in range(10 ** (n - 1), 10 ** n):
    isNarcissus(i)