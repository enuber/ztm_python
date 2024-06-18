# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

import random
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} seconds')
        return result
    return wrapper


li = list(set([random.randint(1, 10000)
          for _ in range(random.randint(1500, 2000))]))
num = random.randint(1, 10000)


@performance
def find_num(li, num):
    return num in li


num_in_list = find_num(li, num)
print(f'The random number {num} was found in the list: {num_in_list}')


@performance
def binary_search_find_num(sorted_li, num):
    # print(sorted_li, num)
    low = 0
    # note that arrays are 0 based so though length of array gives us the total length, the final position in the array is one less
    high = len(sorted_li) - 1

    while low <= high:
        # / is standard division that would be a float, doing // gives back an integer rounded
        mid_point = (low + high) // 2
        guess = sorted_li[mid_point]

        if guess == num:
            return mid_point

        if guess > num:
            high = mid_point - 1
        else:
            low = mid_point + 1

    return -1


li.sort()
result = binary_search_find_num(li, num)

if result != -1:
    print(f"The number {num} was found in the list at index {result}")
else:
    print(f'The number {num} was not found in the list')
