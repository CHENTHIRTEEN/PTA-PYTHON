letter, blank, digit, other = 0, 0, 0, 0
s = input()
while 1:
    for i in s:
        if i.isalpha():
            letter += 1
        elif "0"<=i<="9":
            digit += 1
        elif i == ' ' or i == '\n':
            blank += 1
        else:
            other += 1
    if letter + blank + digit + other >= 10:
        break
    blank += 1
    s = input()
print(f'letter = {letter}, blank = {blank}, digit = {digit}, other = {other}')


# letter,blank,digit,other=0,0,0,0
# s=input()
# while 1:
#     for i in s:
#         if i.isalpha():
#             letter=letter+1
#         elif "0"<=i<="9":
#             digit=digit+1
#         elif i==" " or i=="\n":
#             blank=blank+1
#         else:
#             other=other+1
#     if letter+digit+blank+other>=10:
#         break
#     blank=blank+1
#     s=input()
# print("letter = %d, blank = %d, digit = %d, other = %d"%(letter,blank,digit,other))
