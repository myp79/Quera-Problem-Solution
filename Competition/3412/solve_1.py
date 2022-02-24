def place(alpha):
    if alpha == 'L':
        return 0


l = []
for i in range(4):
    person = list(input().split())
    if person[1] != 'U':
        num = place(person[1])
        if num == 0:
            l.insert(num, person[0])
        else:
            l.append(person[0])

print(l[1])
# Mohammad YousefiPour - Github.com/myp79
