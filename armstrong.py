num=int(input("Enter a number:"))

sum=0
l=len(str(num))
temp=num
while temp>0:
    digit=temp%10 #by taking this % symbol last number will assign to digit
    sum+=digit**l
    temp//=10 #by taking this // symbol it will remove decimal point.
if num==sum:
    print("The given number is Armstrong")
else:
    print("The given number is not a Armstrong")