import math
size = list(map(int, input().split()))
result = size[0]/size[1]
if math.modf(result)[0] == 0.0:
    print(int(result))
else:
    print(int(result)+1)

# Mohammad YousefiPour - Github.com/myp79
