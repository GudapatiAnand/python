#check if the first and last number of a list is the same.

numbers_x=[10,20,30,40,10]

def first_last(numbers_x):
    first=numbers_x[0]
    last=numbers_x[-1]
    if first==last:
        return True
    else:
        return False
print(first_last(numbers_x))