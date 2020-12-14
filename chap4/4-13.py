error = float(input())
a = 1
k = 2
i = 2
b = 1 / k
sum = 2
while a - b >= error:
    a = b
    sum += a
    i += 1
    k *= i
    b = 1 / k

print(f'{sum:.6f}')

# import math
# e=float(input())
# a=1
# i=2
# t=2
# b=1/t
# sum=1+1
# while(a-b>=e):
#     a=b
#     sum=sum+a
#     i=i+1
#     t=t*i
#     b=1/t
# print('{:.6f}'.format(sum))
