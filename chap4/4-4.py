import math
def isPrimer(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range(2, n // 2 + 1):
    z = n - i
    if isPrimer(z) and isPrimer(i):
        print(f'{n} = {i} + {z}')
        break




# import math
# def isPrime(n):
#   if n <= 1:
#     return False
#   for i in range(2, int(math.sqrt(n)) + 1):
#     if n % i == 0:
#         return False
#   return True

# x=int(input())
# for y in range(2,x//2+1):
#     z = x - y
#     if (isPrime(y) == 1 and isPrime(z) == 1):
#         print('{:d} = {:d} + {:d}'.format(x, y, z))
#         break


# import math
# n = int(input())
# primer = []
# num1 = []
# num2 = []
# for i in range(1, n + 1):
#     isPrimer = True
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             isPrimer = False
#             break
#     if isPrimer:
#         primer.append(i)

# primer.sort()
# for i in range(1, len(primer)):
#     for j in range(i, len(primer)):
#         if primer[i] + primer[j] == n:
#             #print(f'{n} = {primer[i]} + {primer[j]}')
#             num1.append(primer[i])
#             num2.append(primer[j])
#             break

# print(f'{n} = {num1[0]} + {num2[0]}')
