n = int(input())
sazman = []
for i in range(n):
    sazman.append(input())

k = int(input())
s = set()
result = 0
for i in range(k):
    name = input()
    s.add(name)
    if len(s) == n:
        result += 1
        s.clear()
        s.add(name)
print(result)
n = int(input())
sazman = []
for i in range(n):
    sazman.append(input())

k = int(input())
s = set()
result = 0
for i in range(k):
    name = input()
    s.add(name)
    if len(s) == n:
        result += 1
        s.clear()
        s.add(name)
print(result)

# Greedy Approach
# Mohammad YousefiPour - Github.com/myp79
