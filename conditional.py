'''
decision making statements

if
else
elif
nested if
shorthand if
shorthand if else
'''


'''
Syntax
if condition:
   Statements
else:   
   Statements
'''

# here If statement is true
# if True:
#    print("i am if")
# else:
#    print("i am else")

# here If statement is False
# if False:
#    print("i am if")
# else:
#    print("i am else")

#elif statement is true
# if False:
#    print("i am if")
# elif True:
#    print("i am elif")    
# else:
#    print("i am else")


#Nested If

# if True:
#    print("outer if")
#    if True:
#        print("inner if")
#    else:
#        print("inner else")
# else:
#    print("outer else")    

# Sample

# Age=18

# if Age>18:
#     print("you can Vote")
# elif Age==18:
#     print("you can Vote buddy")
# else:
#     print("wait")     

#Shorthand if
#if condition:statement
# if 5>2:print("this is if")

#Shorthand if else
#Statement if condition else Statement
# print("this is if") if 5>2 else print("this is else")
# print("this is if") if 5<2 else print("this is else")

n=int(input("Enter the number:"))
print("Even") if n%2==0 else print("Odd")