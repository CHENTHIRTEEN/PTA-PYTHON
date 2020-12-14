string = input()
print(string)
flag = 0
for i in range(0, len(string)):
    if string[i] == string[0 - (i + 1)]:
        flag = 1
    else:
        break
if flag == 1:
    print('Yes')
else:
    print('No')