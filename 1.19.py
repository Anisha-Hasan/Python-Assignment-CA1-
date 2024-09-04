#print sum of digits

n=int(input("Enter a number: "))
sum=sum(int(digit) for digit in str(n))
print("The sum of digits is: ",sum)