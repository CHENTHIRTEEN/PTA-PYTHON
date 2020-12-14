# def Full_Permutation(t):
#     out = []
#     if len(t) == 1:         # 当只有一个元素的时候排列只有一个，直接返回
#         return [t]
#     for j in t:
#         t_copy = t.copy()
#         t_copy.remove(j)    # 移除元素j，对其余元素全排递归
#         out += [[j] + k for k in Full_Permutation(t_copy)]
#     return out
 
 
# t_ = [i for i in range(1, int(input()) + 1)]    # 生成前n位数
# res = Full_Permutation(t_)
# for m in res:
#     print("".join([str(n) for n in m]))

def Permutation(num):
    nums = []
    if len(num) == 1:
        return [num]
    for i in num:
        num2 = num.copy()
        num2.remove(i)
        nums += [[i] + j for j in Permutation(num2)]
    return nums

n = int(input())
num = []
for i in range(1, n + 1):
    num.append(i)
nums = Permutation(num)
for i in nums:
    print(''.join([str(n) for n in i]))