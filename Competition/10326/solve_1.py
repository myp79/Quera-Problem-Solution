nums = list(map(int, input().split()))
result = [0, 0, 0, 0]
i = 0
j = 0
while(not 0 in nums):
    nums[j % 4] -= 1
    result[i % 4] += 1
    i += 1
    j -= 2

for i in result:
    print(i, end=' ')

# Mohammad YousefiPour - Github.com/myp79
