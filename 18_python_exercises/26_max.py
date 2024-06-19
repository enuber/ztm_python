# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

import random

# *args allows you to bring in an undetermined amount of arugments


def find_max(*args):
    nums = list(args)
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


numbers_list = [random.randint(0, 1000000)
                for _ in range(random.randint(200, 30000))]

print(find_max(2, 4, 6, 7, 10, 4))
# the * before numbers_list passes the list in as separate arguments
print(find_max(*numbers_list))
