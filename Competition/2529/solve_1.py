n = int(input())
top = 0
count = 0
for i in range(n):
    d = {}
    count = 0
    word = input()
    for index in word:
        d[index] = d.get(index, 0) + 1

    for row in d.keys():
        count += 1

    if count > top:
        top = count

print(top)
# Mohammad YousefiPour - Github.com/myp79
