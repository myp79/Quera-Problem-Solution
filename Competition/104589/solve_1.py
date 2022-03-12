n = int(input())
if n % 2 == 0:
    print(n//2)
else:
    dev = []
    for i in range(1, n):
        if n % i == 0:
            dev.append(i)
    print(max(dev))
# Mohammad YousefiPour - Github.com/myp79
