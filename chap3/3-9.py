s = '123456789abcdefABCDEF'
string = input()
value = ''
for i in string:
    if i in s:
        value += i

if value == '':
    print('0')
elif string.find(value[0]) > string.find('-'):
    print(-int(value,16))
else:
    print(int(value,16))

# str1 = input()
# s = '1234567890abcdefABCDEF'
# c = ""
# for item in str1:
#     if item in s:
#         c = c + item
 
# # print(str1.find(c[0]))
# # print(str1.find('-'))
# if c == '':
#     print('0')
# elif str1.find(c[0])>str1.find('-'):    
#     print(-int(c,16))
# else:
#     print(int(c,16))