#find the roots of quadratic equation

#ax**2+bx+c=0

import cmath
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
dis=b**2-(4*a*c)
sol1=(-b+cmath.sqrt(dis))/(2*a)
sol2=(-b-cmath.sqrt(dis))/(2*a)
print("The solution is: ",sol1,sol2)