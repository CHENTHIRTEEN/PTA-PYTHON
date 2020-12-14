n = int(input())
num = []
for i in range(0, n):
    flag = True
    m = int(input())
    for j in range(0, m):
        num = list(map(int, input().split()))
        for k in range(0, m):
            if j > k and num[k] != 0:
                flag = False
                break
    if flag:
        print('YES')
    else:
        print('NO')


# a=int(input())
# for i in range(0,a):
#     n=int(input())
#     flag=1
#     for j in range(0,n):
#         s=list(map(int,input().split()))
#         for k in range(0,n):
#             if j>k and s[k]!=0:
#                 flag=0
#                 break
#     if flag==0:
#         print("NO")
#     else:
#         print("YES")   
