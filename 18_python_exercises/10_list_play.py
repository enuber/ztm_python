# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

import random
a = [5, 10, 15, 20, 25]

b = random.sample(range(1, 50), 15)

c = [random.randint(1, 100) for _ in range(random.randint(10, 20))]


def first_last_of_list(li):
    return [li[0], li[-1]]


print(a, first_last_of_list(a))
print(b, first_last_of_list(b))
print(c, first_last_of_list(c))
