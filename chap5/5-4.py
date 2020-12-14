vote = set(list(input().split(',')))
num = []
for i in range(6, 11):
    if str(i) not in vote:
        num.append(i)
    
print(' '.join(map(str, num)))
# for i in num:
#     if i not in vote:
#         pass