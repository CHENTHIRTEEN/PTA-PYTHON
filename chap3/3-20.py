num = list(input())
isFirst = 1
num.reverse()
for i in range(0, len(num)):
    if num[i] == '0' and isFirst == 1:
        continue
    else:
        print(num[i], end = '')
        isFirst = 0