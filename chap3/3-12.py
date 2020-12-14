n = int(input())
temp = n
k = 0
num = 0
while temp != 0:
    num += temp % 10
    temp = temp // 10
    k += 1

print(f"{k} {num}") 