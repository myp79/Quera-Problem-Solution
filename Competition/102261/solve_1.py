from math import sqrt, floor
n = int(input())
result = []
for i in range(n):
    l, m = tuple(map(int, input().split()))
    x = floor(sqrt(m)) - floor(sqrt(l - 1))
    result.append(x)

for index in result:
    print(index)
# Mohammad YousefiPour - Github.com/myp79
