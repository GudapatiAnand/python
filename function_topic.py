#simple fuction
# def anand():
#     print("this is function")
# anand()

#Single parameter function
# def anand(a):
#     print("this is function",a)
# anand(100)

#Multiple parameter function
# def anand(a,b,c):
#     print("this is function",a,b,c)
# anand(100,33,34)

#we can call the function many times
# def anand(a,b):
#     print(a+b)
# anand(100,33)
# anand(10,33)

#using input method
# def leela(name):
#     print("hi",name)
# n=input("Enter the name:")
# leela(n)


#arbitary arguments(parameters)
#it will save in tuple format
# def leela(*name):
#     print("hi",name)
# leela(1,2,3,4,5,6)


#keyword arguments(parameters)
#it will save in dictionary format
# def leela(**name):
#     print("hi",name)
# leela(name="ram", age=25)


#nested function
# def outer_function():
#     print("this is the outer function")
#     def inner_function():
#         print("this is the inner function")
#     inner_function()
# outer_function()


#we writen the function here and called function in example program using import
#here we use return insted of print you can see the example program to see the output
# def add(a,b):
#     return a+b
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)


#Lambda Functions

# x=lambda a,b,c: a+b*c
# print(x(1,2,3))


# l1=[12,34,5,6,8] #list
# l2=[] #new empty list
# for i in l1: #[12,34,5,6,8] 
#     t=lambda a:a+1
#     l2.append(t(i))
# print(l2)


#filter function
#Syntax filter(function,sequence)

# ages=[5,12,17,18,24,32]

# def myfun(x):
#     if x >= 18:
#         return True
#     else:
#         return False
    
# adults=filter(myfun,ages)
# print(list(adults))

#map function
#syntax map(function,iteration)

# def caladd(n):
#     return n+n
# numbers=(1,2,3,4)
# result=map(caladd,numbers)
# print(list(result))


#reduce function
#syntax reduce(function, sequence)
# from functools import reduce
# d=reduce(lambda a,b : a+b , [23,21,45,98] )
# print(d)

#generator function
#here we used multiple yield
#yield will pause the execution after value returns.
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3

# xis a generator object
# x=simpleGeneratorFun()

#iterating over the generator object using next
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

#here the multiple return will not work.
#return will terminate the execution after value returns.

# def aa():
#     return 1+1
#     return 2+1
# print(aa())

# diff bw filter and map
# nums=[11,22,33,44,55]
# map=list(map(lambda x: x**2, nums))
# print(list(map))
# filter=list(filter(lambda x:x%2==0, nums))
# print(list(filter))

#squaring the elements using the map and lambda function
list1=[3,4,5,6]
list2=list(map(lambda x: x**2, list1))
print(list2)

