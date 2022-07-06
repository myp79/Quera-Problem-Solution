a = int(input(""))
b = int(input(""))

for i in range(a,b+1):
    if i == 1:
        continue
    cunter = 0
    for j in range(2,i):
        if i % j == 0:
            cunter += 1
    if cunter == 0 :
        print(i)

# Seyed Mojtaba Esmaili - github.com/SMojtabaE