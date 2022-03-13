n = int(input())
k = int(input())
sen = input()
for i in range(k):
    sen = sen[-1]+sen[:-1]
    x = ''
    for j in sen:
        z = (ord(j)+1)
        if z == 123:
            z = 97
        x += chr(z)
    sen = x
print(sen)
# Mohammad YousefiPour - Github.com/myp79
