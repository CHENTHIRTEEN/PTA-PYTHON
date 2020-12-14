x = float(input())
if x == 0:
    print("f({0:.1f}) = {1:.1f}".format(x, 0))
else:
    print("f({0:.1f}) = {1:.1f}".format(x, 1 / x))