def is_exist(start, end, l):
    for i in range(start, end+1):
        if not i in l:
            return False
    return True


n = int(input())
item = []
for i in range(n):
    x = list(map(int, input().split()))
    for i in range(x[0], x[1]+1):
        item.append(i)
start = int(input())
end = int(input())
if is_exist(start, end, item):
    print('true')
else:
    print('false')

# Mohammad YousefiPour - Github.com/myp79
