def dayInYear(m, d):
    s = d
    if m > 6 and m != 12:
        s += 6*31+(m-7)*30
    elif m <= 6:
        s += (m-1)*31
    elif m > 6 and m == 12:
        s += 6*31+(m-7)*30
    return s


m1, d1 = tuple(map(int, input().split()))
m2, d2 = tuple(map(int, input().split()))
calc1 = dayInYear(m1, d1)
calc2 = dayInYear(m2, d2)
print(abs(calc1-calc2))
# Mohammad YousefiPour - Github.com/myp79
