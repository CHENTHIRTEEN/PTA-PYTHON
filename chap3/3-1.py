heigh = input().split()
print(heigh)
for i in range(len(heigh)):
    heigh[i] = int(heigh[i])

print(heigh)
avg = sum(heigh) / len(heigh)

for i in range(len(heigh)):
    if heigh[i] > avg:
        print(heigh[i], end = " ")