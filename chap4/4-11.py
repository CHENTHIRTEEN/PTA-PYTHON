import math
def isPrimer(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = []
n = int(input())
for i in range(0, n):
    k = int(input())
    num.append(k)


for i in range(0, n):
    if isPrimer(num[i]):
        print('Yes')
    else:
        print('No')




    