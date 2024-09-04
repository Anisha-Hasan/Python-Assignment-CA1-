#WAP to find the gravitational force act in between two objects
# Mass of the objects
# Distance between the two object

m1=int(input("Enter mass of first object: "))
m2=int(input("Enter mass of second object: "))
G=6.67*(10**-11)
r=float(input("Enter distance between two objects: "))
f=G*((m1*m2)/r**2)
print("The gravitational gorce is: ",f)