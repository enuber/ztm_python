#  REGEX 3

import re

string = 'anything@anything.com'

# checks for email
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

a = pattern.search(string)
print(a.group())  # anything@anything.com


# REGEX 4

password = 'supersecret%$#8'

password_pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

b = password_pattern.fullmatch(password)
print(b)  # supersecret%$#8
