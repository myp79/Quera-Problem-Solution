elem = list(map(int, input().split()))
d = {}
for i in range(elem[0]):
    words = input().split()
    d[words[0]] = words[1]

words = input().split()
for word in words:
    exist = d.get(word, '')
    if exist != '':
        print("%s kachal!" % (exist), end=' ')
    else:
        print("kachal!", end=' ')
print()
# Mohammad YousefiPour - Github.com/myp79
