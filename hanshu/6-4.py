def fib(n):
    f = 0
    if n == 0 or n == 1:
        return 1
    else:     
        return fib(n - 2) + fib(n - 1)


#1 1 2 3 5 8 13 21 
def PrintFN(m,n):
    flist = []
    for i in range(25):
        if fib(i) <= n and fib(i) >= m:
            flist.append(fib(i))
    return flist

m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
b=fib(i)
print("fib({0}) = {1}".format(i,b))
fiblist=PrintFN(m,n)
print(len(fiblist))