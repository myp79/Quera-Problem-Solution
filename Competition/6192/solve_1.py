a, b, c, d, e, f = tuple(map(int, input().split()))

result = 'dari mimiri'

if result != 'zende mimuni':
    if a >= d:
        if b >= e or b >= f:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

if result != 'zende mimuni':
    if a >= e:
        if b >= d or b >= f:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

if result != 'zende mimuni':
    if a >= f:
        if b >= d or b >= e:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

if result != 'zende mimuni':
    if b >= d:
        if a >= f or a >= e:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

if result != 'zende mimuni':
    if b >= e:
        if a >= d or a >= f:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

if result != 'zende mimuni':
    if b >= f:
        if a >= d or a >= e:
            result = 'zende mimuni'
        else:
            result = 'dari mimiri'

print(result)
# Mohammad YousefiPour - Github.com/myp79
