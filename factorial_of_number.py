n=int(input("Enter any number: "))
fact=1
if n!=0:
    for i in range(1,n+1):
        fact=fact*i
    print(n,"! is", fact)
else:
    print("0! is 1")