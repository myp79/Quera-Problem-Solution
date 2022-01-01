songs = []
songs.append(input().split())
songs.append(input().split())
if songs[0][0] == songs[0][1] or \
        songs[0][0] == songs[1][1] or \
        songs[1][0] == songs[1][1] or \
        songs[1][0] == songs[0][1]:
    print('YES')
else:
    print('NO')
# Mohammad YousefiPour - Github.com/myp79
