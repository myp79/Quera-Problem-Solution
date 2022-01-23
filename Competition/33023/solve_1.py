n, m = tuple(map(int, input().split()))
counter = 0
result = []
for i in range(n):
    result.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and j < m-1 and i < n-1:
            if result[i][j] > result[i-1][j] and result[i][j] > result[i+1][j] and result[i][j] < result[i][j-1] and result[i][j] < result[i][j+1]:
                counter += 1
            elif result[i][j] < result[i-1][j] and result[i][j] < result[i+1][j] and result[i][j] > result[i][j-1] and result[i][j] > result[i][j+1]:
                counter += 1
print(counter)
