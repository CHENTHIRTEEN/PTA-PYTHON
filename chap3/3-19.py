n = int(input())
str1 = []
max = ''
index = 0
for i in range(0, n):
    str1.append(input())

for i in range(0, len(str1)):
    if len(str1[i]) > index:
        index = len(str1[i])
        max = str1[i]

print(f"The longest is: {max}")