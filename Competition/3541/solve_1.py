n = int(input())
bound = (n//2+1)//2
answer = bound*(bound+1) - (n//2)*bound + (n//3)-bound
k = (n//3)//2
answer += (n+1)*k-3*k*(k+1)

if n//3 % 2 == 1:
    answer += (n - 3*(2*k+1)) // 2
print(answer)
# Mohammad YousefiPour - Github.com/myp79
