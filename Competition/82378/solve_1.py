n = int(input())
x = int(input())
cost = 0
if n >= x:
    cost += x*1500
    n -= x
if x > n:
    cost += n*1500
    n = 0
if n > 60:
    cost += 60*1500
    n -= 60
    cost += n*3000
else:
    cost += n*1500


print(cost)

# Mohammad YousefiPour - Github.com/myp79
