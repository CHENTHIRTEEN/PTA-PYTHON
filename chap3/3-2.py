# 查验身份证 (15分)
#数据预处理
M = ('1','0','X','9','8','7','6','5','4','3','2') #校验码
nums = ('0','1','2','3','4','5','6','7','8','9') #自然数集，用于判断前17位是否为数字
weight = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
allPassed_Flag = 0

n = int(input())
for i in range(n):
    aStr = input() #获取输入的待验证数据
    if(len(aStr) > 18):
        print(aStr)
        break
    correct = 0 #判断前17位是否都为数字的标记
    j = 0
    for j in range(0,17):
        if((aStr[j] in nums) == False):
            print(aStr) #前17位不都为数字,输出
            break
    #再筛选前17位都是数字但校验码不正确的身份证
    if(j == 16 and aStr[16] in nums):
        #求z
        zz = 0
        for k in range(0,17):
            zz = zz + int(aStr[k])*weight[k]
        z = int(zz) % 11
        # 判断身份证最后一位是否匹配
        if(aStr[-1] != M[z]):
            print(aStr)
        else:
            allPassed_Flag = allPassed_Flag + 1
if(allPassed_Flag == n):
    print("All passed")