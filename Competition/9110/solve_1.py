def rev(nums):
    l = [nums]
    for i in nums:
        if i == '0':
            l.append('1')
        else:
            l.append('0')
    return ''.join(l)


result = '1'
l, r = map(int, input().split())
while len(result) < r:
    result = rev(result)
print(result[l-1:r])
# Mohammad YousefiPour - Github.com/myp79
