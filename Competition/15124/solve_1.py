def devide(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    return result


a, b, x = tuple(map(int, input().split()))
counter = 0
a_list = devide(a)
b_list = devide(b)
for i in a_list:
    for j in b_list:
        if i+j <= x:
            counter += 1
print(counter)
# Mohammad YousefiPour - Github.com/myp79
