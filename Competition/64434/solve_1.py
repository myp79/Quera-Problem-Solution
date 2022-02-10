n, m = tuple(map(int, input().split()))
pat = False
for i in range(3*n):
    if i == n or i == 2*n:
        pat = not pat
    for j in range(3*m):
        if j == m or j == 2*m:
            pat = not pat
        if pat:
            print('.', end='')
        else:
            print('X', end='')
    print()
# Mohammad YousefiPour - Github.com/myp79
