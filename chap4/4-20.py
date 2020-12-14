m, n = map(int, input().split())
nums = []
for i in range(0, m):
    num = list(map(int, input().split()))
    nums.append(num)

for i in range(0, m):
    print(sum(nums[i]))