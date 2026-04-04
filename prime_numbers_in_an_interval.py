l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))

for i in range (l,u+1):
    c=0
    for x in range(1,i+1):
        if i%x==0:
            c=c+1
    if c==2:
        print(i)