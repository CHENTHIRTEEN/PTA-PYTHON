s = input()
s1, s2 = input().split()

for i in range(len(s) - 1, -1, -1):
    if s[i] == s1:
        print(f"{i} {s1}")
    elif s[i] == s2:
        print(f"{i} {s2}")