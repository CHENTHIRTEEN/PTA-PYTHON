n = input()
m = "AEIOU"
c = 0
for i in n:
    if i not in m and i.isupper() == 1:
        c += 1
print(c)