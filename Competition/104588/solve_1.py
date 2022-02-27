nums = list(map(int, input().split()))
c = 0

for i in nums:
    if i >= 80:
        c += 1

if c >= 3:
    print('Mamma mia!')
elif c >= 1 and c <= 2:
    print('Mamma mia!!')
else:
    print('Mamma mia!!!')
# Mohammad YousefiPour - Github.com/myp79
