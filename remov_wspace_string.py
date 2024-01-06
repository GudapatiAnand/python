#python program to remove whitespace from a string

import re

text='Gudapati      Anand'
print("Orginal Text:",text)
print("After removing whitespace:",re.sub(r'\s+','',text))