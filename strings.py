'''
collection of characters
'''
#types of declearing string
# a='pythonlife'
# b="pythonlife's"
# v='''python
# life
# in'''
# print(type(a),type(b),type(v))
# print(a)
# print(b)
# print(v)

'''
lower()
upper()
endswith()
startswith()
replace()
find()
index()
count()
remove prefix()
remove suffix()
split()
strip()
rstrip()
lstrip()
Format()
isalnum()
isalpha()
join()
title()
'''

# a='gudapati anand'
# print(a.upper())
# b='GUDAPATI ANAND'
# print(b.lower())
# print(a.endswith("anand"))
# print(a.endswith("g"))
# print(a.startswith("gudapati"))
# print(a.startswith("d"))
# print(a.replace('anand', 'Anand'))
# print(b.index('ANAND'))
# print(b.find('ANAND'))
# #print(b.index('anand'))
# print(b.find('anand'))
# print(b.count('A'))
# print(b.removeprefix('GUDAPATI'))
# print(b.removesuffix('ANAND'))
# print(b.split())
# print(len(a))


# a="   Gudapati Anand   "
# print(a)
# print(len(a))
# b=a.strip()
# print(len(b))
# b=a.lstrip()
# print(len(b))
# b=a.rstrip()
# print(len(b))



# a="hi {} thinara?".format("Anand")
# print(a)

names=["leela", "Anand", "Priya", "Sai","santhosh"]
for i in names:
    print("hi {} thinara?".format(i))

# a="Anand"
# print(a.isalnum())
# print(a.isalpha())

# a="Anand123"
# print(a.isalnum())
# print(a.isalpha())

# b="poor dad rich dad"
# print(b.title())


# k=" hi this is is my car"
# print(k.replace(" is", " are",1))
# v=k.replace(" is", " are").replace("this", "that")
# print(v)

# d="this is string class"
# print(d)
# c=d.split()
# print(c)
# s=" ".join(c)
# print(s)




# d="this is string class"
# f=d.split()
# n=[]
# for i in f:
#     if i=="is":
#         i="are"
#         n.append(i)
#     elif i=="this":
#         i="that"
#         n.append(i)  
#     else:
#         n.append(i)
# print(n)    