from functools import reduce

# useful functions to help with functional programming

# MAP

# map(action/function, itterable/data)


my_list = [1, 2, 3]
# function just needs to return the data now. No longer need to create a list and append to it and then return the list. it effectively goes over the itterable data one by one and does something to it and we return the result.

# pure function as doesn't modify anything outside and always returns expected data.


def multiply_by2(num):
    return num * 2


# printing just the map will give you a map object with memory location. Since we are sending in a list, we can create a list from what is returned and print that.
print(list(map(multiply_by2, my_list)))  # [2,4,6]
print(my_list)  # [1,2,3] - doesn't effect the original list.

# FILTER
# filtering the results

# gives back only items that are odd. does a true false check and filter only adds things that are true.


def only_odd(num):
    return num % 2 != 0


print(list(filter(only_odd, my_list)))  # [1,3]
print(my_list)  # [1,2,3] - again doesn't effect the original list

# ZIP
# need to lists or itterables and zip them together. Can combine as many itterables together as you have. not limited to just two.
# may not seem that useful but think of a database where we need to combine columns. If they are in same order then zipping will grab them in order and combine them into tuples quickly.

your_list = [10, 20, 30]

# [(1, 10), (2, 20), (3, 30)] - gives list of tuples
print(list(zip(my_list, your_list)))
print(my_list)  # [1,2,3] doesn't effect original list.


# REDUCE
# doesn't come built in, have to import it in to use, check top of this page to see the import line
# from functools import reduce

# acc is short for accumulator. We set it to what it is as the third argument being passed into the function. In this case it's the 0 from the below call.
# when this runs first time, acc=0 num=1, next time it calls acc=1 num=2, then acc=3 num=3 and final result is 6 which is ultimately what is returned.
def accumulator(acc, num):
    return acc + num


print(reduce(accumulator, my_list, 0))  # 6


# EXERCISES

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize_list(word):
    return word.capitalize()


print(list(map(capitalize_list, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def passing(num):
    return num > 50


print(list(filter(passing, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def find_total(acc, num):
    return acc+num


combined_list = (my_numbers + scores)

print(reduce(find_total, combined_list, 0))
