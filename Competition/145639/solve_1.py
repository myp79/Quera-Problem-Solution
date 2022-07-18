s, f, l, x = map(int, input().split())
if x < s:
    print('exam did not started!')
elif x >= f:
    print('exam finished!')
else:
    print(min(f-x, l))
