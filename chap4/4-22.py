n = int(input())
num = []
nums = []
a, b = 0, 0
max = 0
for i in range(n):
    num = list(map(int, input().split()))
    nums.append(num)

for i in range(n):
    if a == n and b == n:
        break
    for j in range(n):
        for k in range(n):
            if nums[i][j] >= nums[i][k]:
                a += 1
        if a == n:
            for l in range(n):
                if nums[i][j] <= nums[l][j]:
                    b += 1
            if b == n:
                print(f"{i} {j}")
                break
        a, b = 0, 0
if a != n and b != n:
    print("NONE")

# n = int(input())
# a = []
# count = 0
# count1 = 0
# for i in range(n):
#     s = input()
#     a.append([int(n) for n in s.split()])
# for j in range(n):
#     if count1 == n and count == n:
#         break
#     for k in range(n):
#         for k1 in range(n):
#             if a[j][k] >= a[j][k1]:
#                 count += 1
#         if count == n:
#             for j1 in range(n):
#                 if a[j][k] <= a[j1][k]:
#                     count1 += 1
#             if count1 == n:
#                 print("{} {}".format(j, k))
#                 break
#         count1 = 0
#         count = 0
# if count1 != n and count != n:
#     print("NONE")
   

#     4
# 1 7 4 1
# 4 8 3 6
# 1 6 1 2
# 0 7 8 9