n = int(input())
caps = False
result = []
for i in range(n):
    text = input()
    if text == 'CAPS':
        caps = not caps
        continue
    if caps:
        result.append(text.upper())
    else:
        result.append(text.lower())
print(''.join(result))
# Mohammad YousefiPour - Github.com/myp79
