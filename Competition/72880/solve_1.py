e = list(map(int, input().split()))

if e[4]*e[2]+e[0] >= e[4]*e[3]+e[1]:
    if e[4]*e[2] >= e[4]*e[3]:
        print('Eyval baba!')
    else:
        print('Naaa, eshtebahe!')
elif e[4]*e[2] <= e[4]*e[3]:
    print('Eyval baba!')
else:
    print('Naaa, eshtebahe!')
# Mohammad YousefiPour - Github.com/myp79
