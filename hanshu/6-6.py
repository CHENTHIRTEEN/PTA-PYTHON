def acronym(phrase):
    s = ''
    lis = phrase.split()
    for i in lis:
        s += i[0]
    return s.upper()


phrase=input()
print(acronym(phrase))