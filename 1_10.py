#Take input from user(as integer) if it greater than 15 then print two times are diffrent, if it
# is less than 15 print 4 times are diffrent

a=int(input("Enter a number:"))
if(a>15):
    print((a-15)*2)
elif(a<15):
    print(4*(15-a))
else:
    print("Invalid")