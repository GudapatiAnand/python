# try:
#     print("a")
# except:
#     print("error vachindi")
# else:
#     print("error raledhu")
# finally:
#     print("always")


# try:
#     print('a'+10)
# except Exception as anand:
#     print("error occured",anand)


#try block will not handle multiple errors 
# try:
#     print('a'+10)
# except NameError:
#     print("Name error occured")
# except TypeError:
#     print("Type error occured")


#Nested try block

# try:
#     print('a'+10)
# except:
#     print("outer")
#     try:
#         print(a)
#     except:
#         print("inner")


#indentation error
# if True:
#     print("this is")


#Type error
# s=1+'d'
# print(s)

#key error
# d={1:"a"}
# print(d[2])

#index error
# c=[1,2,4,6,9,3]
# print(c[100])


#keyboardinterrupt error
# while True:
#     print("looop")


#syntax error
# d=[1,2,3,4,5
# print(d)


#FileNotFoundError
# f=open("kiran.txt",mode='r')


#ModuleNotFoundError
#import anand

#ValueError it will occur when you enter input otherthan int
# c=int(input())
# print(c)


#ZeroDivisionError
#print(1/0)


#AttributeError
# i=1000000
# i.append(100)

#type error
# def func(a):
#     print(a)
# func(1,2)
