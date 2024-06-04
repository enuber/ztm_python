# debugging

# linting - use a linter

# learn to read errors and understand what they mean.

# python debugger
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 'hhkhads')

# in pdb you can type help to see all the commands available
# step - allows you to go line by line within pdb in terminal
# continue - lets you go through a function until you return something
# a - shows you a list of arguments
# exit - to get to of pdb

# can look at the documentation.  https://docs.python.org/3/library/pdb.html
