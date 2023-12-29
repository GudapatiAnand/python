#if the number is divided by 2 then the remainder is 0 then it is even
#if the remainder is 1 then it is odd.
num=int(input("Enter the number:"))

if num%2==0: # we are checking the reminder is 0 or not
    print("{} is Even".format(num))
else:
    print("{} is Odd".format(num))