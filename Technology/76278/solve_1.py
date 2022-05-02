def calculator(n, m, li):
    result = []
    i = 0
    min = 1
    s = 0
    while i < n:
        if not i+m > n-1:
            result.append(sum(li[i:i+m]))
        else:
            result.append(sum(li[i:]))
        i = i+m

    for i in result:
        s += min*i
        min *= -1
    return s


print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
# Mohammad YousefiPour - Github.com/myp79
