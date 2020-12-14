s = list(map(int, input().split()))
num = []
nums = []
for i in range(len(s)):
    num.append(s[i])
    if (i + 1) % 3 == 0:
        nums.append(num)
        num = []

for i in range(3):
    for j in range(3):
        print(f'{nums[j][i]:>4}', end = '')
    print()