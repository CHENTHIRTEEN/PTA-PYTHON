m, n = map(int, input().split())
nums = []
flag = True
for i in range(m):
    num = list(map(int, input().split()))
    nums.append(num)

for i in range(1, m - 1):
    for j in range(1, n - 1):
        if nums[i][j] > nums[i - 1][j] and nums[i][j] > nums[i + 1][j] and nums[i][j] > nums[i][j - 1] and nums[i][j] > nums[i][j + 1]:
            print(f'{nums[i][j]} {i + 1} {j + 1}')
            flag = False
if flag:
    print(f'None {m} {n}')