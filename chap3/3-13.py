ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str1 = list(input())
index = 0
for i in range(0, len(str1)):
    if str1[i].isalpha():
        if str1[i] >= 'A' and str1[i] <= 'Z':
            index = ch.find(str1[i])
            str1[i] = ch[-(index + 1)]
            print(str1[i], end = '')
        else:
        #     temp = str1[i]
        #     temp = temp.upper()
        #     index = ch.find(temp)
        #     str1[i] = ch[-(index + 1)].lower()
            print(str1[i], end = '')
    else:
        print(str1[i], end = '')

# Only the 11 CAPItaL LeTtERS are replaced.
# Lmob gsv 11 CZKRgzO OvGgVIH ziv ivkozcvw.

# Lnly the 11 XZKRtaO OeGtVIH are replaced.
# Lnly the 11 CZKRtaO OeGtVIH are replaced.