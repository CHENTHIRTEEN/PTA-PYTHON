n = int(input())

s = sum([1 / (i * 2 - 1) for i in range(1, n + 1)])
print("sum = {:.6f}".format(s))