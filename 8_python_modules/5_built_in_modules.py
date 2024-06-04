# python comes with built in modules. when you install python you get them. You just have to import them.

# https://docs.python.org/3/py-modindex.html

# good practice to only import what you are using rather than whole library so that other devs will know you are only using specific methods.
import random
import sys

# help(random)

print(dir(random))  # gives you list of tmethods

print(random.random())
print(random.randint(1, 10))  # gives random int between two numbers
print(random.choice([1, 2, 3, 4]))  # gives random choice from specific items

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# sys.argv - gives you access to materials in the terminal window so if we were to do
# python3 5_built_in_modules.py erik nuber
# note that the file name itself is in sys.argv[0]
first = sys.argv[1]
last = sys.argv[2]
print(f'hi, {first} {last}')
