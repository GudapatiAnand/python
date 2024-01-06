#python program to access index of a list using for loop start the indexing with non zerovalue

my_list=[25,30,77,38]
for index,val in enumerate(my_list,start=1):
    print(index,val)
