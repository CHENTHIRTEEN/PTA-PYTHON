m, n = map(int, input().split())
s = 0
s = sum([i * i for i in range(m, n + 1)])

s += sum([1 / i for i in range(m, n + 1)])
print("sum = {:.6f}".format(s))