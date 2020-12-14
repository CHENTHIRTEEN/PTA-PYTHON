n = int(input())
sum = 0
nums = []
for i in range(0, n):
    num = list(map(int, input().split()))
    nums.append(num)
for i in range(0, n):
    for j in range(0, n):
        if i != n - 1 and j != n - 1 and i + j != n - 1:
            sum += nums[i][j]
print(sum)