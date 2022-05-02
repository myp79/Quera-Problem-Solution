from math import sqrt


def prime(x):
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n, m, k = tuple(map(int, input().split()))
x = y = 0
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))

for i in range(k):
    z = nums[x][y]
    if prime(z):
        x = (x*-1)+n-1
        y = (y*-1)+m-1
    else:
        if z % 4 == 0:
            if y+1 == m:
                y = 0
            else:
                y += 1
        elif z % 4 == 1:
            if x+1 == n:
                x = 0
            else:
                x += 1
        elif z % 4 == 2:
            if y-1 < 0:
                y = m-1
            else:
                y -= 1
        elif z % 4 == 3:
            if x-1 < 0:
                x = n-1
            else:
                x -= 1
print(x+1, y+1)
# Mohammad YousefiPour - Github.com/myp79