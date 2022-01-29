n, x, k = tuple(map(int, input().split()))
channel = []
for i in range(n):
    channel.append(input())
if x+k > n:
    print(channel[(x+k) % n-1])

elif x+k <= n:
    print(channel[x+k-1])
# Mohammad YousefiPour - Github.com/myp79
