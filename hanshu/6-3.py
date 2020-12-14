def CountDigit(number, digit):
    return str(number).count(str(digit))



number,digit = input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number,digit )
print("Number of digit 2 in "+str(number)+":",count)