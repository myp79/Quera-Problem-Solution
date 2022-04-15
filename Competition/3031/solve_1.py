n, k = tuple(map(int, input().split()))
fruit = []
for i in range(n):
    b, a = tuple(map(int, input().split()))
    fruit.append([b, a])

fruit.sort(key=lambda x: x[0])
for i in range(n):
    if fruit[i][0] <= k and fruit[i][0] < fruit[i][1]:
        k += fruit[i][1]-fruit[i][0]

print(k)
# Greedy Approach
# Mohammad YousefiPour - Github.com/myp79
