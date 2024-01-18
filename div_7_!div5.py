'''
findall the numbers which are divisible by 7 but are not divisible by 5 in the range of 0-1000
'''

l=[]
for i in range (0,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(','.join(l))