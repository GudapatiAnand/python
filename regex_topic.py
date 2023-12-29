# 
#raw string 
# r=r"python \n programming"
# print(r) 

import re 

# address="78 Hi 11 89 Main, 4th cross, 123, Marthalli, 5678 Banglore, 560023 67893"
# add_no=re.findall(R'\d+',address)
# print(f'sorting the only nums from address {add_no}')

# ## now i want nos with 6 digit only
# #REAL LIFE APPLICATION - EXTRACTING THE PIN CODE
# add_dig=re.findall(r'\d{6}',address)
# print(f'sorting the only nums from address {add_dig}')

# # now i want nos with 2 digit only
# add_dig=re.findall(r'\d{2}',address)
# print(f'sorting the only nums from address {add_dig}')

# # now i want nos with 1-6 digit only
# add_dig=re.findall(r'\d{1,6}',address)
# print(f'sorting the only nums from address {add_dig}')

# import re

# s='''Current IP Address Allocation
# IP Address are 172.45.78.109
# loopbook Address:127.0.0.1
# Computer 1:10.67.89.101
# Computer 2:11.67.98.102
# Computer 3:12.68.98.102
# '''

# ip_s=re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',s)
# print(f'ip address are -:{ip_s}')

# ### 10 or 11 (first method)
# ip_s1=re.findall(r"1[0-1]\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
# print(f'ip address are -:{ip_s1}')

# ### 10 or 11 (second method)
# ip_s1=re.findall(r"1[0|1]\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
# print(f'ip address are -:{ip_s1}')

# ### 10 or 11 (third method)
# ip_s1=re.findall(r"1[01]\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
# print(f'ip address are -:{ip_s1}')

# ## 10 only
# ip_s1=re.findall(r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
# print(f'ip address are -:{ip_s1}')

# ## 11 only
# ip_s1=re.findall(r"11\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
# print(f'ip address are -:{ip_s1}')


# print("find all matches for format Month day")

# matches=re.findall(r"[A-Z][a-z]+\s\d{1,2}","These are the match dates June 24, August 9, Dec 12")
# print(f'gives Month Date format-{matches}')

# # it gives only date not months
# matches=re.findall(r"[A-Z][a-z]+\s(\d{1,2})","These are the match dates June 24, August 9, Dec 12")
# print(f'gives Month Date format-{matches}')

# #it gives month and date seperately in string
# matches=re.findall(r"([A-Z][a-z]+)\s(\d{1,2})","These are the match dates June 24, August 9, Dec 12")
# print(f'gives Month Date format-{matches}')


# s="purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _@gmail.com"
# emails=re.findall(r"\w+@\w+\.\w+",s)
# print(emails)

# s="purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _@gmail.com"
# emails=re.findall(r"[A-Za-z]+@\w+\.\w+",s)
# print(f'Starts with alphabets only: {emails}')

# s="purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _@gmail.com"
# emails=re.findall(r"\d+@\w+\.\w+",s)
# print(f'Starts with digits only: {emails}')


# #findall digit one or more
# new_str="Friend in need is 23 friend in 453214 deed"
# nr3=re.findall('\d+',new_str)
# print(nr3)

#search() returns only the first match to the pattern from the target string

# target_string="Emma is a python developer \n Emma also knows ML and AI"
# #caret(^) matches at the beginning of a string
# result=re.search(r"^\w{4}",target_string)
# print(result.group())


# str1="Emma is a python developer \n Emma also knows ML and AI"
# result=re.search(r"\w{2}$",target_string)
# print(result.group())

#st='In a world where you can be anything, be kind'

# match_object=re.search('In',st)
# print(f'type is object{match_object}')

# match_object1=re.search('be',st)
# print(f'type is object{match_object1}')

# print(match_object.start()) 
# print(match_object1.start()) 

# print(match_object.span())
# print(match_object1.span())

# source_str='we need to inform him with the latest information'

# info=re.search('inform',source_str)
# print(info)

# if re.search('inform',source_str):
#     print('inform is there')

# randomstr='here is \\kane'

# print(randomstr)

# print(re.search(r'\\kane',randomstr))

# split
#re.split() method split the string by the occurences of the regex pattern, returning a list containing the resulting substring.

# st='In a world where you can be anything, be kind'
# r=re.split(' ',st)
# print(r)

# r1=re.split('e',st)
# print(r1)

# r2=re.split('e',st,2)
# print(r2)

# s='Welcome to regex programming using Python'
# print(f'the value of s   :{s}')

# lstval=re.split(r'\s',s)
# #\s only one space
# print(f'Regex Split value of s    :{lstval}')

# lstval2=re.split(r'\s+',s)
# #\s one or more spaces
# print(f'Regex Split value of s    :{lstval2}')

#sub()- substitute  *sub('old pattern','new pattern',source_str)
# st='In a world where you can be anything, be kind'
# sb=re.sub('e','E',st)
# print(sb)

# sb1=re.sub('e','E',st,2)
# print(sb1)

#Compile()
#The re.compile() method changed the string pattern into a re.Pattern object that we can work upon.

# a='hat mat rat pat'
# reg=re.compile('[r]at')

# rplce=reg.sub('FOOD',a)
# print(rplce)

# #replacing
# rplc=re.sub('rat','FOOD',a)
# print(rplc)


#Working with white Spaces

# a='''keep the blue flag
# flying high
# chelsa
# '''
# print(a)

# new_str=re.sub('\n',' ',a)
# print(new_str)

# #other method using compile
# comp=re.compile('\n')
# new=comp.sub(' ',a)
# print(new)

# phone_no='''
# 444-122-1234
# 123-122-78999
# 111-123-23
# 67-7890-2019
# '''
# #3 digit @start &middle, end-4 digit

# reg=re.findall(r'\d{3}\-\d{3}\-\b\d{4}\b',phone_no)
# print(reg)

#Match
#re.match() method looks for the pattern only at the beginning of the target string 

target_string="Jessy loves Python and Pandas"
#Match six-letter word
pattern=r'\w{6}'

#match() method
result=re.match(pattern,target_string)
print(result)

#search() method
result=re.search(pattern,target_string)
print(result.group())

#findall() method
result=re.findall(pattern,target_string)
print(result)