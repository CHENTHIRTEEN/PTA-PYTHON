a, b = map(int, input().split())
k = 0
s = sum([i for i in range(a, b + 1)])
for i in range(a, b + 1):
    k += 1
    if k % 5 == 0:
        print(f"{i:>5}")
    else:
        print(f"{i:>5}",end = "")
if k % 5 == 0:
    print(f"Sum = {s}")
else:
    print()
    print(f"Sum = {s}")