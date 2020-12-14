n = int(input())
if n == 0:
    print('average = 0.0')
    print('count = 0')
    exit(0)
    
scores = list(map(int, input().split()))
average = 0
count = 0
for i in range(0, n):
    average += scores[i] / n
    if scores[i] >= 60:
        count += 1

print(f'average = {average:.1f}')
print(f'count = {count}')

