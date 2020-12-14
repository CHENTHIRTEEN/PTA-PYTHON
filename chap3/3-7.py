n = int(input())
nums = list(map(int, input().split()))

index = {}

for i in range(len(nums) - 1, -1, -1):
    index[nums[i]] = i

max_value = max(index.keys())
for keys, values in index.items():
    if keys == max_value:
        print(keys, values)
