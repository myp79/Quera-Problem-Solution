x = input()
nums = [int(a) for a in x]
number = list(range(int(x)+1, 10**len(x)))
out = []
for i in number:
    num = [int(a) for a in str(i)]
    if sorted(num) == sorted(nums) and int(x) < i:
        out.append(i)
if len(out) == 0:
    print(0)
else:
    print(out[0])
# Mohammad YousefiPour - Github.com/myp79
