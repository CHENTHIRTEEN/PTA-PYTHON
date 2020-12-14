n = int(input())
num = 0
sum = 0
for i in range(n):
    dic = eval(input())
    for j in dic:
        temp = dic[j]
        for key in temp:
            num += 1
            sum += temp[key]
print(f'{n} {num} {sum}')