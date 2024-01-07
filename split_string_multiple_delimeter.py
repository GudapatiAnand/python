#Python program to split string with multiple delimiters

import re

text="the quick brown\nfox jumps*over the lazy dog."

print(re.split(';|\*|\n',text))