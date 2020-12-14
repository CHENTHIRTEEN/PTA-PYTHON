str1 = list(input())
value = ''
l = len(str1)
for i in range(len(str1)):
    if str1[i].isalpha() and str1[i] != ' ' and value.count(str1[i].upper()) + value.count(str1[i].lower()) == 0:
        value += str1[i]
    if len(value) == 10:
        print(value)
        break

if len(value) < 10:
    print('not found')

#This is a test example