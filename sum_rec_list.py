#Write a python program of recursion list sum.

def recursive(data_list):
    total=0
    for ele in data_list:
        if type(ele)==type([]):
            total+=recursive(ele)
        else:
            total+=ele
    return total
print(recursive([1,2,[3,4],[5,6]]))
