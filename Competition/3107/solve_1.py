size = list(map(int, input().split()))
person = list(map(int, input().split()))
if size[0] >= person[0]:
    if size[1] >= person[1]:
        print('yes')
    else:
        print('no')
else:
    print('no')
# Mohammad YousefiPour - Github.com/myp79
