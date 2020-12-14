s = eval(input())
s1 = list(set(s))
num = []
for i in s:
    if i in s1 and i not in num:
        num.append(i)
print(' '.join(map(str, num)))



# for i in num:
#     if i in num1 and i not in num2:
#         num2.append(i)
# for i in range(0, len(num2)):
#     if i != len(num2) - :
#         print(num2[i], end = ' ')
#     else:
#         print(num2[i], end = '')
