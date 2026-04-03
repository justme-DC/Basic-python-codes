p=int(input("Enter the principal amount: "))
r=int(input("Enter interest rate: "))
t=int(input("Enter the time period of loan: "))

print("Simple interest is", p*r*t/100)
print("Amount is", p+p*r*t/100)