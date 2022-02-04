n = int(input())
d = {}
for i in range(n):
    word = input().split()[0]
    d[word] = d.get(word, 0)+1

print(max(d.values()))
# Mohammad YousefiPour - Github.com/myp79
