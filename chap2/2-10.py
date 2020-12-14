lower, upper = map(int, input().split())

if lower > upper or upper > 100:
    print("Invalid.")
else:
    print("fahr celsius")
    for i in range(lower, upper + 1, 2):
        print("{:d}{:>6.1f}".format(i, 5 * (i - 32) / 9))