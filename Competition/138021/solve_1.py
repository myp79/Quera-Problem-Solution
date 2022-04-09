def ischeck(n, z):
    x, y = 0, 0
    for i in range(1, n+1):
        x = i
        y = a-i
        if x > y+z or y > x+z or z > x+y:
            return 'YES'
    return 'NO'


a, b = map(int, input().split())


if a > b:
    z = b
    print(ischeck(a, z))
else:
    z = a
    print(ischeck(b, z))
# Mohammad YousefiPour - Github.com/myp79
