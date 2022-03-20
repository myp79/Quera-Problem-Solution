def ischeck(arr):
    for i in range(1, n-1):
        index = arr[i]
        if(arr[i-1] < index and arr[i+1] < index):
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))

if ischeck(arr):
    print('Ey baba :(')
else:
    print('Bah Bah! Ajab jooji!')
# Mohammad YousefiPour - Github.com/myp79
