s = list(map(int, input().split()))
num = []
nums = []
for i in range(len(s)):
    num.append(s[i])
    if (i + 1) % 3 == 0:
        nums.append(num)
        num = []
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(f'{nums[i][j]:>4}', end = '')
    print(f'{max(nums[i]):>4}', end = '')
    print(f'{sum(nums[i]):>4}')