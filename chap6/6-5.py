def getSum(s, weight):
    sum = 0
    for i in s:
        if isinstance(i, int):
           sum += weight
        else:
            sum += getSum(i, weight + 1)
    return sum
    
s = eval(input())
weight = 1
sum = getSum(s, weight)
print(sum)