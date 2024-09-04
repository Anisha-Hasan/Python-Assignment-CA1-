#Implement a simple calculator

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
operator=input("Enter operation you want to perform:(+,-,/,%,*): ")
if(operator == "+"):
    print("Sum is:",(a+b))
elif(operator == "-"):
    print("Substraction is:",(a-b))
elif(operator == "/"):
    print("Division is:",(a/b))
elif(operator == "%"):
    print("modulo is:",(a%b))
elif(operator == "*"):
    print("Product is:",(a*b))
else:
    print("Invalid")