# file=open("demo.txt",mode='r')
# c=file.read()
# print(c)
# file.close()

# file=open("demo.txt",mode='r')
# c=file.readline()
# print(c)
# file.close()

# file=open("demo.txt",mode='r')
# c=file.readlines()
# print(c[0]) #index c[0]
# file.close()

# file=open("demo.txt",mode='w')
# c=file.write("this is my write function")
# file.close()


# file=open("demo.txt",mode='a')
# c=file.write(" this is my append mode")
# file.close()


#Reading file in r+ mode
# with open('demo.txt','r+') as f:
#     print(f.tell())
#     print(f.read())
#     print(f.tell())


#Reading file in w+ mode in this we can perform read operation only after the write operation is done.
# with open('demo.txt','w+') as f:
#     print(f.tell())
#     c=f.write("this is w+")
#     print(f.read())
#     print(f.tell())


#Write file in 'r+' mode
# with open('demo.txt','r+') as f:
#     f.write("new text.")


#write file in 'w+' mode
with open('demo.txt','w+') as f:
    f.write("new text.")


#opening file in 'w+' mode when it does not exist
# with open('anand.txt','w+') as f:
#     pass


# #opening a file
# f=open('demo.txt','r')
# print(f.tell())
# f.read(2)

# #printing the position
# print(f.tell())
# f.seek(0)
# print(f.tell())
# # closing file
# f.close()


file=open('demo.txt',mode='r+')
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(2,"chetan")
print(file.tell())
file.close()
file=open('demo.txt',mode='w')
print(f)
for i in f:
    file.writelines([i])