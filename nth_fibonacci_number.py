n=int(input("Enter any number: "))
L=[1,1]
x=1
while x!=n:
    L.append(L[x]+L[x-1])
    x=x+1
print(L[n-1])