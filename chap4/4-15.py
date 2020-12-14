n = int(input())
#sum0 = [1, 1, 1, 0]
#sum  = sum0
count = 0
for i in range(n // 5, 0, -1):
    for j in range(n // 2, 0, -1):
        for k in range(n, 0, -1):
            if 5 * i + 2 * j + 1 * k == n:
                print(f'fen5:{i}, fen2:{j}, fen1:{k}, total:{i + j + k}')
                count += 1
print(f'count = {count}')
