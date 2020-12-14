n = int(input())
s = 65
for i in range(n, 0, -1):
    for j in range(i):
        print(f'{chr(s)}', end = ' ')
        s += 1
    print()