# Atm using functions

name="anand"
password="123"
user_name=input("enter user name:")
password1=input("enter password:")
s='''
1.credit
2.debit
3.ministatement
4.exit
'''
def credit():
    credit_amount=float(input("enter the Amount:"))
    print("Amount after credit:",Amount+credit_amount)

def debit():
    debit_amount=float(input("enter the Amount:"))
    print("Amount after credit:",Amount-debit_amount)

Amount=1000
if name==user_name and password==password1:
    while True:
        print(s)
        option=int(input("enter the option:"))
        if option==1:
            credit()
        elif option==2:
            debit()
        elif option==3:
            print("Amount",Amount)
        elif option==4:
            break       
else:
    print("incorrect password or username")
