# calculator using functions

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print('''
1.add
2.sub
3.mul
4.div
''')
select=int(input("Please select the operation you need to perform:"))
if select==1:
    print(a,"+",b,"=",add(a,b))
elif select==2:
    print(a,"-",b,"=",sub(a,b))
elif select==3:
    print(a,"*",b,"=",mul(a,b))
elif select==4:
    print(a,"/",b,"=",div(a,b))
else:
    print("invalid input")