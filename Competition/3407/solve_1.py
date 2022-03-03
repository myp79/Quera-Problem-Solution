n, m = tuple(map(int, input().split()))
k = int(input())
result = []
for i in range(n):
    result.append([0] * m)

for i in range(k):
    x, y = tuple(map(int, input().split()))
    result[x-1][y-1] = '*'

for i in range(n):
    for j in range(m):
        counter = 0
        if result[i][j] != '*':
            if i > 0 and j > 0 and i+1 < n and j+1 < m:
                if result[i-1][j-1] == '*':
                    counter += 1
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j+1] == '*':
                    counter += 1
                if result[i][j-1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
                if result[i+1][j-1] == '*':
                    counter += 1
                if result[i+1][j] == '*':
                    counter += 1
                if result[i+1][j+1] == '*':
                    counter += 1
            elif i == 0 and j == 0:
                if result[i+1][j] == '*':
                    counter += 1
                if result[i+1][j+1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
            elif i+1 == n and j == 0:
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j+1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
            elif i == 0 and j+1 == m:
                if result[i+1][j] == '*':
                    counter += 1
                if result[i+1][j-1] == '*':
                    counter += 1
                if result[i][j-1] == '*':
                    counter += 1
            elif i+1 == n and j+1 == m:
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j-1] == '*':
                    counter += 1
                if result[i][j-1] == '*':
                    counter += 1
            elif i == 0 and j < m and j > 0:
                if result[i][j-1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
                if result[i+1][j-1] == '*':
                    counter += 1
                if result[i+1][j] == '*':
                    counter += 1
                if result[i+1][j+1] == '*':
                    counter += 1
            elif j == 0 and i < n and i > 0:
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j+1] == '*':
                    counter += 1
                if result[i+1][j] == '*':
                    counter += 1
                if result[i+1][j+1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
            elif i+1 == n and j < m and j > 0:
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j+1] == '*':
                    counter += 1
                if result[i-1][j-1] == '*':
                    counter += 1
                if result[i][j-1] == '*':
                    counter += 1
                if result[i][j+1] == '*':
                    counter += 1
            elif j+1 == m and i < n and i > 0:
                if result[i-1][j] == '*':
                    counter += 1
                if result[i-1][j-1] == '*':
                    counter += 1
                if result[i][j-1] == '*':
                    counter += 1
                if result[i+1][j-1] == '*':
                    counter += 1
                if result[i+1][j] == '*':
                    counter += 1
            result[i][j] = counter

for row in result:
    for col in row:
        print(col, end=' ')
    print()


# Mohammad YousefiPour - Github.com/myp79
