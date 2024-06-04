from functools import reduce

# lambda expressions
# one time anonymous functions you only use once.

# lambda param: action(param)

my_list = [1, 2, 3]

# this is it. take an item from the my_list, pass it into the lambda as item and then take that item and multiply it by two. It automatically gets returned.
print(list(map(lambda item: item * 2, my_list)))  # [2,4,6]

print(list(filter(lambda item: item % 2 != 0, my_list)))  # [1,3]

print(reduce(lambda acc, item: acc + item, my_list))  # 6


# EXERCISE

# Square
my_list = [5, 4, 3]

print(list(map(lambda num: num**2, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

# remember sort does it in place so print it after to show the sorted list properly.
# sort() take a key to determine what to sort by. we want it sorted by the second number in the tuple
# we are simply saying here with the lambda that x is the tuple and, from that tuple we want to use what is in the second place which because of zero indexing is x[1]
a.sort(key=lambda x: x[1])
print(a)
