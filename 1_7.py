#convert given number of days into years,month,week,days

day=int(input("Enter number of days: "))
year=day//365
month=(day-(year*365))//30
din=(day-(year*365)-(month*30))
print("Year=",year)
print("Month=",month)
print("Days=",din)