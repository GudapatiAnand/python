'''
list
'''

# a=[1,2,2.3,5,"anand"]
# print(a)
# print(a[2])
# print(a[-1])
# print(a[0:4:2])

#anand=[] #empty list
# anand=list()
# print(type(anand))

# anand=[1,2.2,'python',True] #method 1
#anand1=list(1,2.2) if we give like this we will get error
#list() method we will use only in type conversion
# anand1=list([1,2.2])#method 2
# print(anand)
#print(anand1)

#anand=[2,4,7,6,8,4,'False']
#slicing
#[start:stop:skip]
#print(anand[0:5])
#print(anand[2:2]) # it will give empty list
# print(anand[5:0]) #this will not work if we want to do this we need skip
#print(anand[0:5:2])
#print(anand[0:5:-2])# this will not work because backward skiping will not work
#print(anand[5:0:-2])
#print(anand[-1:-5:-2])
#print(anand[-1:-5:2]) #this will not work because backward skiping will not work
#print(anand[0:5:3])
#print(anand[:5]) #before index 5
#print(anand[5:]) #after index 5
#print(anand[::]) #prints all the data 
#print(anand[:]) #it also prints all the data
#print(anand[:-1])
#print(anand[::-1]) #it will reverse the list 

# anand=[2,4,7,6,8,4,'False']
# anand[0]='hi'
# print(anand)


'''
append()
copy()
clear()
extend()
count()
insert()
pop()
remove()
index()
reverse()
sort()

Syntax

variable.method()
'''
#a=[1,2,2.3,5,"anand"]
#a.append("gudapati")
#a.append(["gudapati"]) # it will add like sub list inside the list
#a.extend([4,5,6,7,8,9])
#a.extend(4,5,6,7,8,9) # this will give the error 
#print(a)
#print(a.count(2))
# a.remove(6)
# print(a)
# a.pop(2) # in pop we need to give index to delete
#a.remove(2.3) # in remove we need to give element to delete
#a.reverse()
#print(a)
#a.clear()
#print(a)
#print(a.index(2))
#print(len(a))
# for i in a:
#     print(i)

# a=[1,2,2.3,5,"anand"]
# a.insert(0,3)
# print(a)

# a=[1,2,2,2.3,5,"anand"]
# b=a.copy()
# a.append('hi')
# print(b)
# print(a)

# a=[1,21,3,49,5,16,7,38,94]
# a.sort() # by default it will give assending order
# a.sort(reverse=True) # to get decending order
# print(a)

# list=["even" if i % 2==0 else "odd" for i in range(10)]
# print(list)

fruits=["apple", "banana","cheery","kiwi","mango"]
newlist=[x for x in fruits if "a" in x ]
print(newlist)