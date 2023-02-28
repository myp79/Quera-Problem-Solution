t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    if l[0]+l[2]>l[1]+l[3]:
        print('perspolis')
    elif l[0]+l[2]<l[1]+l[3]:
        print('esteghlal')
    elif l[0]+l[2]==l[1]+l[3]:
        if l[0]<l[3]:
          print('perspolis')
        elif l[3]<l[0]:
            print('esteghlal') 
        else:
            print('penalty')
# Mohammad YousefiPour - Github.com/myp79