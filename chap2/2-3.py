n = int(input())

if n < 0:
    print("Invalid Value!")
elif n <= 50:
    print("cost = {:.2f}".format(n * 0.53))
else:
    print("cost = {:.2f}".format(50 * 0.53 + (n - 50) * 0.58))