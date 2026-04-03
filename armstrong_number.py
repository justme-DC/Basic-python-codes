#checking for armstrong number
n=int(input("Enter any number: "))
s=n #storing the value.
k=s #Might need it later

#section 1 where we will calculate digits
d=0
while n!=0:
    n=n//10
    d=d+1

#section 2 where we will do the main thing

c=0
while s!=0: #not using n because it is 0
    x=s%10
    c=x**d+c
    s=s//10

if c==k:
    print("given number is an armstrong number")
else:
    print("given number is not an armstrong number")