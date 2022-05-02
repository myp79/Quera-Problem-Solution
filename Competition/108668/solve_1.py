n, m, k = tuple(map(int, input().split()))
arr = [[[]for i in range(m)]for j in range(n)]
counter = 1
for i in range(k):
    r, c, l = tuple(map(int, input().split()))
    for j in range(l):
        for k in range(l):
            arr[r-1+j][c-1+k].append(counter)
    counter += 1
result = []
for i in range(n):
    for j in range(m):
        if not arr[i][j] in result and arr[i][j] != []:
            result.append(arr[i][j])
print(len(result))


# Dynamic Programming
# Mohammad YousefiPour - Github.com/myp79
