def separator(ls):
    odd = []
    even = []
    for item in ls:
        if item % 2 == 0:
            odd.append(item)
        else:
            even.append(item)
    return (odd, even)
# Mohammad YousefiPour - Github.com/myp79
