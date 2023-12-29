punctuation='''"'!@#$%^&*,.:;'''
str=input("Enter the string:")

new_str=" "
for c in str:
    if c not in punctuation:
        new_str+=c
print(new_str)