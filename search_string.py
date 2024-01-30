#check that a string contains only a certain set of characters.

import re #regular expression

def is_allowed(string):
    char=re.compile(r'[^a-zA-Z0-9]')
    str=char.search(string)
    return not bool(str)
print(is_allowed("Abcd1234"))
print(is_allowed("##^$*$((#"))