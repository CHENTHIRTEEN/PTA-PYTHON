import math
def PrimeSum(m, n):
    sum = 0
    if m == 1:
        m += 1
    for i in range(m, n + 1):
        isPrimer = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                isPrimer = False
                break
        if isPrimer:
            sum += i
    return sum



m,n=input().split()
m = int(m)
n = int(n)
print(PrimeSum(m,n))