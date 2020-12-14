def judge(s):
    l = []
    for i in s:
        if isinstance(i, (tuple, list)) and not isinstance(i, str):
            for j in judge(i):
                l.append(j)
        else:
            if not isinstance(i, str):
                l.append(i)
    return l

s = eval(input())
num = [i for i in judge(s)]
print(sum(num))