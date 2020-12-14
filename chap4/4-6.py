n = int(input())
f = 1
f1 = 1
k = 2
if n < 1:
    print('Invalid.')
else:
    if n <= 2 and n >= 1:
        for i in range(0, n):
            print(f'{f:>11}', end = '')
    else:
        print(f'{f:>11}', end = '')
        print(f'{f:>11}', end = '')
        for i in range(2, n):
            k += 1
            f1, f = f, f + f1
            if k == 5:
                print(f'{f:>11}')
                k = 0
            else:
                print(f'{f:>11}', end = '')
        


