dic = {"+":"x + y", "-":"x - y", "*":"x * y", "/":"x / y if y != 0 else 'divided by zero'"}
x = int(input())
op = input()
y = int(input())
r = eval(dic[op])
if type(r) != str:
    print(f'{r:.2f}')
else:
    print(r)