#check wheather a given year is leap or not

year=int(input("Enter year: "))
if(year%4==0):
    print("Leap year")
elif(year%400==0):
    print("Leap year")
elif(year%100==0):
    print("Leap year")
else:
    print("Not leap year")