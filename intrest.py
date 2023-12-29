'''
p=principal amount
t=time in days
r=rate of interest
si=simple intrest
Ci=compond intrest
'''
# p=10000
# t=365
# r=5
# si=(p*t*r)/100
# print(si)


# we can give the inputs in the time of execution using input method
p=int(input("enter the Amount:"))
t=int(input("enter the time in days:"))
r=int(input("enter the rate of interest:"))
si=(p*t*r)/100
print(si)
Ci=p*(((1+r/100)**t)-1)
print(Ci)