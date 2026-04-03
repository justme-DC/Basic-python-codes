p=float(input("Enter the principal amount: "))
r=float(input("Enter interest rate: "))
t=int(input("Enter the time period of loan: "))

amount=p*(1+r/100)**t
ci=amount-p

print("Amount is", amount)
print("Compound interest is", ci)