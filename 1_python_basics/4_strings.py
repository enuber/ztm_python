# strings

# a string is a piece of text stored in quotation marks 

print(type("this is a string!"))
username = "supercoder"
# long string allows you to write code on multiple lines and uses the three quote marks to demark it.
password = "supersecret"
long_string = '''
WOW
O O 
---
'''

print(long_string);

first_name = 'erik'
last_name = 'nuber'
full_name = first_name + ' ' + last_name
print(full_name) # erik nuber <--- contats with the + sign

# string concatenation
# simply means adding strings together
print('hello', first_name) # hello erik
print('hello ' + first_name) # hello erik
# print('hello' + 5) # gives error because it is an int and a str
print(type(str(100))) # will give type str because we are making 100 a string.

# type conversion
# allows you to change the type something is using str(), int()...

# escape sequence
weather = 'It\'s sunny' # use the \ to allow for escape a character so that it appears as it should. whatever comes after the \ is a string is the idea.
print(weather) # It's sunny

# special cases
# \t will make a tab 
# \n will create a new line

# Formatted strings aka fstring

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old.') # hi Johnny. You are 55 years old.

# python2 way that works in 3
print('hi {}. You are {} years old.'.format(name, age))
print('hi {1}. You are {0} years old.'.format(name, age)) # by using the numbers you are telling it the order the variables should appear so here age would appear first and then name as it is zero based.


# better way to do this (this is correct way)
# this does the same as above but using "f" makes it a formatted string and you can use variables inside curly braces.
print(f'hi {name}. You are {age} years old.')

# String indexes
# below shows ways you can slice a string up.

selfish = 'me me me' #each letter and space is stored in a different space in memory
# 01234567 <--this is the order for 'me me me'
print(selfish[0]) # m  this gives the first letter as it is zero-based, more specifically it is saying take the variable selfish, and with the [0] grab the item at index 0.

# when you use [start:stop] you are saying start at one spot and go until you reach the stop but don't include that
print(selfish[0:2]) # me will give you the first two letters

# can add in a stepover [start:stop:stepover], stepover tells you how many places to skip basically. 
print(selfish[0:8:2]) #m em <-- grabs first one, then skips two which takes us to space, grabs the space, then skips two which takes you to e, grabs that, then skips two which takes you to m, then skips two which takes you past string and thats it.
print(selfish[1:]) # e me me  <---- will start at index 1 and give everything after
print(selfish[:5]) # me me <---- will give everything from start up until index of 5 but not including 5.
print(selfish[::1]) # me me me <---- will start from the begining, not stop and will stepover every letter which is the default behaviour so get everything.
print(selfish[::3]) # mmm 
print(selfish[-1]) # e  <--- start from end of string and in this case give last letter
print(selfish[::-1]) #em em em <---- get the reverse of the string


# Immutability
# strings are immutable, you can't change them using indexes.

# can be done
selfish1 = 'you you you'
selfish1 = 'me me me'
print(selfish1 + ' you')

# can't be done, only way to change a string is complete reassignment
# selfish1[0] = 'm'



# built in functions and methods
# there are many built in functions
# https://docs.python.org/3/library/functions.html
# and methods
# https://www.w3schools.com/python/python_ref_string.asp

greet = 'hello'
print(len(greet)) # 5 <--len gives the length len is a function
greet.capitalize() #Hello <--this is a method that capitalizes a string

quote = 'to be or not to be'
print(quote.upper()) # TO BE OR NOT TO BE
print(quote.capitalize()) # To be or not to be
print(quote.find('be')) # 3 <--- gives the index where the word starts at the first time.
print(quote.replace('be', 'me')) #to me or not to me <-- replaces all occurances.
print(quote) # to be or not to be  <-- remember string is immutable so not being reassigned and the "me" doesn't stay in effect.