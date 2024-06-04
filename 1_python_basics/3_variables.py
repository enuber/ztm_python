# variables video

# a way to store information we need to use 

iq = 190 # variable name is iq and can be used later
print(iq) # example using it 

# best practice

"""
snake_case
start with lowercase or underscore
letters, numbers, underscores
case sensitive
don't overwrite keywords
"""

_user_IQ = 190 # ex snake_case, also starting with underscore. Underscore represents a private variable.

# gotchas with variables

PI = 3.14 # by starting it with capital letters, saying this is a constant variable and shouldn't be changed.

__variablename__ = 'hi' # shouldn't use double underscores 

a, b, c = 1, 2, 3 # fast way to assign variables 


#expressions / statements video

iq = 100
user_age = iq/5 # expression is iq/5 that produces a value. so an expression produces a value. the entire line of code is the statement that does an action. user_age = iq/5 is a statement.


# augmented assignment operator

some_value = 5 
some_value = some_value  + 2
some_value += 2 # same as above and is called an augmented assingment operator can be done with + - * / keep in mind that variable already has to be defined first and have a value.
