# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
# List properties
# In other words, “things you can do with lists.”

# One of the interesting things you can do with lists in Python is figure out whether something is inside the list or not. For example:

#   >>> a = [5, 10, 15, 20]
#   >>> 10 in a
#   True
#   >>> 3 in a
#   False


import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for num in a:
    if num in b and num not in c:
        c.append(num)

print(c)
print(list((set(a).intersection(set(b)))))

# different ways to generate random numbers
d = random.sample(range(1, 50), 15)
e = [random.randint(1, 100) for _ in range(random.randint(10, 20))]

print(list((set(d).intersection(set(e)))))
