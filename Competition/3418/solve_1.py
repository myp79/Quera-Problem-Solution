def findMaxGCD(arr, n):

    high = 0
    for i in range(0, n):
        high = max(high, arr[i])

    count = [0] * (high + 1)
    for i in range(0, n):
        count[arr[i]] += 1

    counter = 0

    for i in range(high, 0, -1):
        j = i

        while (j <= high):

            if (count[j] > 0):
                counter += count[j]

            j += i

            if (counter == 2):
                return i
        counter = 0


n = int(input())
nums = list(map(int, input().split()))

print(findMaxGCD(nums, n))
# Mohammad YousefiPour - Github.com/myp79
