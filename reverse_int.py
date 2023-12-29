num=int(input("Enter the integer to be reverse:"))
reverse_num=0
while num!=0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num//=10
print("integer after reverse:"+str(reverse_num))