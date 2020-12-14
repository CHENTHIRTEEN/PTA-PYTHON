a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.pop(0)
b.pop(0)
c = []
for i in a:
    if i not in b and i not in c:
        c.append(i)
for i in b:
    if i not in a and i not in c:
        c.append(i)
print(" ".join(map(str, c)))
