#Python function that accepts a string and calculate the number of uppercase and number of lowercase in the given string

def string_test(s):
    d={'Upper_case':0,'Lower_case':0}
    for i in s:
        if i.isupper():
            d['Upper_case']+=1
        elif i.islower():
            d['Lower_case']+=1
        else:
            pass
    print("Upper case Letters:",d['Upper_case'])
    print("Lower case Letters:",d['Lower_case'])
string_test("This is Python Life Channel")