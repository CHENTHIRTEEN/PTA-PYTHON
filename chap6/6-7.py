def getSum(s):
    sum = 0
    for i in range(2, len(s)):
        sum += int(s[i])
    return sum

n = int(input())
info = []
s1 = []
max = 0
for i in range(n):
    s = input().split()
    sum = getSum(s)
    if max < sum:
        max = sum
        s1 = s
print(f'{s1[1]} {s1[0]} {max}')