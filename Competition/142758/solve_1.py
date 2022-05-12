n = int(input())
arr = [i for i in range(1, n+1)]

arr.sort()
arr[0], arr[-1] = arr[-1], arr[0]

for i in arr:
    print(i, end=' ')

# Mohammad YousefiPour - Github.com/myp79
