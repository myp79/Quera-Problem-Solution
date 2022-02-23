n = int(input())
for i in range(n):
    x, y = tuple(map(int, input().split()))
    if x == y or abs(x-y) == 2:
        if x % 2 == 0 and y % 2 == 0:
            print(x+y)
        else:
            print(x+y-1)
    else:
        print(-1)
# Mohammad YousefiPour - Github.com/myp79
