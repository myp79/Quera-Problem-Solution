row = list(map(int, input().split()))
if row[0] > row[1]:
    for i in range(row[0]-row[1]):
        print('L', end='')

elif row[0] == row[1]:
    print('Saal Noo Mobarak!')

else:
    for i in range(row[1]-row[0]):
        print('R', end='')
# Mohammad YousefiPour - Github.com/myp79
