#Accept marks of a student of 4 diffrent subjects. Find the average depending on average
# find the grade(if marks>=75, grade A)
#if marks>=60 & <55 grade B
#or marks >=40 & <60 grade is C
#or marks <40 grade is D

a=int(input("Enter marks of Maths:"))
b=int(input("Enter marks of Science:"))
c=int(input("Enter marks of English:"))
d=int(input("Enter marks of SST:"))
avg=(a+b+c+d)/4
print("The average is:",avg)
if(avg>=75):
    print("Grade A")
elif(avg>=60 and avg<55):
    print("Grade B")
elif(avg>=40 and avg<60):
    print("Grade C")
elif(avg<40):
    print("Grade D")
else:
    print("Invalid")