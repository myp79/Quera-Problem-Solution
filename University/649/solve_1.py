a = int(input(""))
b = int(input(""))
notFirst = True 
for i in range(a,b):
    if i == 1 or i == a:
        continue
    cunter = 0
    for j in range(2,i):
        if i % j == 0:
            cunter += 1
    if cunter == 0:
        if i !=a and not notFirst:
            print(","+ str(i),end="")
        else:
            print(i,end="")
            notFirst = False

# Seyed Mojtaba Esmaili - github.com/SMojtabaE