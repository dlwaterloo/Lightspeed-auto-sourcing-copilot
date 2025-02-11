import re

text = "This is a test, with multiple: separators; and some|pipes"
delimiters = ",|:|;|\|"
result = re.split(delimiters, text)
print(result)