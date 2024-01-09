#Python program to calculate the length of string

t="Python is the best programming language"

def string_length(str):
    count=0
    for char in str:
        count+=1
    return count
print(string_length(t))