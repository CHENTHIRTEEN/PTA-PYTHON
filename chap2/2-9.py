num = [0, 0, 0]
num[0], num[1], num[2] = map(int, input().split())
num.sort()
for i in range(0, 3):
    print(num[i], end = "")
    if i < 2:
        print("->", end = "")