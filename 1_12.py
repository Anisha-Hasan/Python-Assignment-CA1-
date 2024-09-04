#check wheather a tringle is equilateral,scaler,isoceles

a=int(input("Enter first side of triangle: "))
b=int(input("Enter second side of triangle: "))
c=int(input("Enter third side of triangle: "))
if(a==b and b==c):
    print("Equilateral triangle")
elif(a==b or b==c or a==c):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")