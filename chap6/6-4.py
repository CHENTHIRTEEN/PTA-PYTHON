def judge(s, weight):
    num = []
    for i in s:
        if isinstance(i, list):
            for j in judge(i, weight + 1):
                num.append(j)
        else:
            num.append(i * weight)
    return num

s = eval(input())
weight = 1
nums = [i for i in judge(s, weight)]
print(sum(nums))