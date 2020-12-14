index = input()
s = input()

for i in range(len(s) - 1, -1, -1):
    if s[i] == index:
        print(f"index = {i}")
        break
    if i == 0:
        print("Not Found")