inp = int(input(""))

sum = 0
for i in range(1,inp):
    if inp % i == 0:
        sum += i
    
if inp == sum:
    print("YES")
else:
    print("NO")
    
# Seyed Mojtaba Esmaili - github.com/SMojtabaE