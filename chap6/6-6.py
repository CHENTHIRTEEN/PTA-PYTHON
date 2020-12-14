def getSum(s, level, weight):
    sum = 0
    if level == weight:
        for j in s:
            if isinstance(j, int):
                sum += 1
    else:
        for j in s:
            if isinstance(j, list):
                sum += getSum(j, level, weight + 1)
    return sum

s = eval(input())
level = int(input())
weight = 1
sum = getSum(s, level, weight)
print(sum)