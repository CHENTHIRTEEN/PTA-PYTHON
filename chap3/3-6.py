res = []
counts = {}
lst = list(map(int,input().split()))
t = lst[1: lst[0]+1]
for word in t:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
word, count = items[0]
print ("{:d} {:d}".format(word, count))