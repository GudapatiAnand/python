#Python program to triple all numbers of given list of integers using map

num=(1,2,3,4,5,6,7)
result=map(lambda x:x+x+x,num)
print(list(result))