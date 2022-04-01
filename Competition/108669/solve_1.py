n, a, b = tuple(map(int, input().split()))
goals = list(map(int, input().split()))


def check(goals):
    for i in range(len(goals)):
        if goals[i] > 45+a and goals[i] < 90:
            if goals[i] > min(goals[i:]):
                return 'NO'
        elif goals[i] > 90+b:
            return 'NO'
    return 'YES'


print(check(goals))
# Mohammad YousefiPour - Github.com/myp79
