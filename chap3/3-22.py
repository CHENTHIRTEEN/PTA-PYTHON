string = input()
value = ''
for i in range(0, len(string)):
    if string[i].isupper() and value.count(string[i]) == 0:
        value += string[i]

if len(value) > 0:
    print(value)
else:
    print('Not Found')