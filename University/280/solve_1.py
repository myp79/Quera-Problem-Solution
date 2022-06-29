
a = int(input())
b = int(input())
c = int(input())

result1 = (a**2) == (b**2) + (c**2)
result2 = (b**2) == (a**2) + (c**2)
result3 = (c**2) == (b**2) + (a**2)

if result1 or result2 or result3 :
    print("YES")
else :
    print("NO")

# Seyed Mojtaba Esmaili - github.com/SMojtabaE