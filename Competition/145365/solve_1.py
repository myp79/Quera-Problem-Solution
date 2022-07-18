n, m = map(int, input().split())
matrix = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = matrix[y-1][x-1] = 1
for i in range(n):
    for j in range(n):
        if matrix[i][j] != 1:
            matrix[i][j] = 0
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='')
    print()
# Mohammad YousefiPour - Github.com/myp79
