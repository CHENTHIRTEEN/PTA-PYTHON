# s1 = input().strip()
# s2 = input().strip()
# s1 = s1.replace(s2.upper(), '').replace(s2.lower(), '')
# print("result: {}".format(s1))


str1 = list(input().strip())
ch = input().strip()


print('result: ', end = '')
for i in range(len(str1)):
    if str1[i] == ch or str1[i] == ch.upper() or str1[i] == ch.lower():
        continue
    else:
        print(str1[i], end = '')