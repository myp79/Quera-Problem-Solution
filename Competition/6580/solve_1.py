x, y = tuple(map(int, input().split()))
r = int(input())
dx, dy = tuple(map(int, input().split()))

if dx >= x and dx <= x+r and dy <=y and dy >= y-r:
    print('Mahdi')
else:
    print('Parsa')
# Mohammad YousefiPour - Github.com/myp79
