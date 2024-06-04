# Generators
# allow us to generate a sequence of values over time

from time import time

range(100)  # this is a generator for example


def make_list(num):
    result = []
    # range itself being a generator isn't holding any place in memory
    for i in range(num):
        result.append(i*2)
    return result


# my_list is taking up space in memory.
my_list = make_list(50)
print(my_list)


# GENERATORS PART 2

# a list is an itterable. any object in python that we can loop through. It means we take one item from the list do something to it and then go on to the next one.
# generators are actually itterable. But not everything that is iterable is a generator. A generator is a subset of itterable. A list is iterahble but is not a generator. Range is a generator is itterable because it gives us numbers one after the other.

# this is a generator, it uses yield to allow us to go one by one through
def generator_function(num):
    for i in range(num):
        # key term, yield pauses the function and comes back to it when we come back to it using next
        yield i


for item in generator_function(50):
    print(item)  # gives us 0 to 49

# if you do
g = generator_function(100)
print(g)  # will give you the function itself which is a generator
# next is another keyword and is how we go through the generator to get back the next value.
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2

# note: if you run out of numbers in the range of the generator you wil get an error StopIteration which means that there is nothing to go next(g) too.


# GENERATORS PERFORMANCE


# will tell us how long a function takes to complete.

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} seconds')
        return result
    return wrapper


@performance
def long_time():
    print('1')
    # nothing is created in memory it goes through using a generator
    for i in range(1000000):
        i*5


@performance
def long_time2():
    print('2')
    # this creates a list in memory and then goes through that one by one.
    for i in list(range(1000000)):
        i*5


long_time()
# takes longer because it is making a list first. close to 2x's as long.
long_time2()
