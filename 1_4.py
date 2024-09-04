#compute simple interest(principle,time,rate and input by user)

principle=float(input("Enter principle amount:"))
time=int(input("enter time:"))
rate=int(input("Enter rate of interest: "))
SI=(principle*time*rate)/100
print("The Simple interest is: ",str(SI))