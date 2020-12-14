s = input()
nums = []
h = 0
flag = 0
for i in range(0, len(s)):
    if s[i] >= '0' and s[i] <= '9':
        nums.append(int(s[i]))
for i in range(0, len(nums) - 1):
    if nums[i] == 0 and flag == 0:
        continue
    else:
        print(nums[i], end = '')
        flag = 1
print(nums[-1])