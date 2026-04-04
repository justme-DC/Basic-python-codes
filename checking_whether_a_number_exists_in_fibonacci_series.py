n=int(input("Enter any number: "))
if int((5*n**2+4)**(1/2))==(5*n**2+4)**(1/2):
    print("Yes given number is in fibonacci series")
elif int((5*n**2-4)**(1/2))==(5*n**2-4)**(1/2):
    print("Yes given number is in fibonacci series")
else:
    print("Given number is not in fibonacci series")