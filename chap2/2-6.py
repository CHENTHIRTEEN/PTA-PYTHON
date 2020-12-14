n = int(input())

s = sum([i / (2 * i - 1) if i % 2 == 1 else - i / (2 * i - 1) for i in range(1, n + 1)])

print("{:.3f}".format(s))