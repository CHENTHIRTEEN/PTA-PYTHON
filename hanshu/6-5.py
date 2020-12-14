import math
def funcos(eps,x):
    sum = 0
    #
    p = 0
    #阶乘值
    p1 = 1
    count = 2
    t = 1
    flag = 1
    while math.fabs(t)>=float(eps):
        sum = sum + t
        p1 = 1
        for i in range(1,count+1):
            p1 = p1*i
        p = p+2
        count+=2
        flag = -flag
        t = flag*x**p/p1
    return sum




eps=float(input())
x=float(input())
value=funcos(eps,x )
print("cos({0}) = {1:.4f}".format(x,value))