#Accept a hyphen- seperated sequence of words as input and prints the sorted words

'''example
input:green-red-black-white
output:black-green-red-white
'''

items=[n for n in input("Enter the string:").split("-")]
items.sort()
print("-".join(items))