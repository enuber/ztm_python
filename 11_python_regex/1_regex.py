# REGEX

import re

string = 'search inside of this text please!'

# you can do this for easy things
print('search' in string)  # True

# <re.Match object; span=(17, 21), match='this'>
# we get more info with the regex search. We find out where it is located in the string.
# if there isn't a match would get back "none"
a = re.search('this', string)
print(a.span())  # (17,21)
print(a.start())  # 17
print(a.end())  # 21

# this - returns the part of the string where there was the match.
print(a.group())

pattern = re.compile('this')
pattern2 = re.compile('search')
string = 'search this inside of this text please!'

# regular search but using pattern which is re.compile('this)
a = pattern.search(string)
b = pattern.findall(string)  # returns every copy of what is being search for
# full match means that what you are searching for has to be exactly what is in the string.
c = pattern.fullmatch(string)
d = pattern2.match(string)  # matches to beginning of string

print(a.group())  # this
print(b)  # ["this", "this"]
print(c)  # None
print(d)  # <re.Match object; span=(0, 6), match='search'>


# REGEX 2
# www.regex101.com
# need to change the language to python

# () - capturing group
# [a-zA-Z] - any letter
# [a] - just the letter a
#  . a single character of any kind including spaces

# ([a-zA-Z]).([a])  # w a - full match

# r here just means its a raw string so ignore what python would assume about the string and just use it as it is
pattern3 = re.compile(r"([a-zA-Z]).([a])")

a = pattern3.search(string)

# sea - because we get a group where there is some letter, any other characters and then the letter "a"
print(a.group())
print(a.group(1))  # s - because of the () we have groups
print(a.group(2))  # a

# https://regexone.com/ - can learn about regex expressions with interactive exercises
