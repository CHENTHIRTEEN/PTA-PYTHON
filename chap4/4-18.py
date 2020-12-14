n = int(input())
if n == 1:
    print('1')
    exit(0)
num = [i for i in range(1, n + 1)]
while len(num) >= 3:
    num.pop(2)
    num.append(num.pop(0))
    num.append(num.pop(0))
print(num[1])



# while len(num) > 1:
#     while index < len(num):
#         num[index - 1] = 0
#         index *= 3
#     index = index - len(num)


#print(num[0])