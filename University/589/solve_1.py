n = int(input())


def fact(x):
    if x == 0 or x == 1:
        return 1
    return fact(x - 1) * x


print(fact(n))

# Mohammad YousefiPour - Github.com/myp79
