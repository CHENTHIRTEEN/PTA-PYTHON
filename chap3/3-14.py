str1 = list(input())

for i in range(0, len(str1) - 1):
    if str1[i].isalpha:
        if 'A' <= str1[i] and str1[i] <= 'Z':
            #str1[i] = str1[i].lower()
            print(str1[i].lower(), end = '')
        else:
            #str1[i] = str1[i].upper()
            print(str1[i].upper(), end = '')
    else:
        print(str1[i], end = '')
