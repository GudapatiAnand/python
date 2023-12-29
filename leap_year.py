def checkyear(year):
    return(((year%4==0) and (year%100!=0) or (year%400==0)))

year=int(input("Enter the year:"))

if (checkyear(year)):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))