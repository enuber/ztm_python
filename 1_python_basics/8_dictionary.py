# Dictionary - an unordered key:value pair. Means they aren't next to eachother in memory. They can be in any order and stored all over in memory.

# dictionaries can store any value, lists, strings, numbers, bool, numbers

# example, key:value pairs
dictionary = {
    'a': 1,
    'b': 2,
    'c': [1, 2, 3]
}

# lets us get value using the key
print(dictionary['b'])  # 2
print(dictionary['c'][2])  # 3


# Fundamentals...

# When to use a list - if you want to have data that has an order, it can hold dictionaries as well.

# When to use a dictionary - if you want to have data that order isn't important. Holds more info because of keys and values.


# Keys
# can be numbers, booleans... key needs to be immutible. Can't be a list because a list can be changed. Most of the time a key is usually a string or something that properly describes what the value will hold. If you have mulitple keys with same name, it will grab the last in the list, they should be unique.

#  Dictionary methods

# get is a method that will get the value if it exists or return None if it doesn't
print(dictionary.get('d'))  # None
# if c doesn't exist will return a default value that you give. If c did exist then it would return c's value instead.
print(dictionary.get('d', 'default_value'))

# can create a dictionary like this though it is uncommon
user = dict(name='erik')
print(user)  # {'name': 'erik'}

print('a' in dictionary)  # True
print('d' in dictionary)  # False

print('c' in dictionary.keys())  # True - checks the keys only
print('2' in dictionary.values())  # False - checks only the value

# dict_items([('a', 1), ('b', 2), ('c', [1,2,3])]) - gives us back all the key value
print(dictionary.items())

# print(dictionary.clear()) # None - clears out the dictionary.

dictionary2 = dictionary.copy()
# can see it is a copy of dictionary. data is separated now so will be an actual individual copy and if it is changed the original won't change.
print(dictionary2)

# print(dictionary.pop('c')) # will remove a specific key value pair and return the value. this mutates

# print(dictionary.popitem()) # removes last key:value pair in dict and returns its value.

print(dictionary.update({'c': [4, 5, 6]}))  # None - nothing gets returned
print(dictionary)  # shows 'c' is updated with new data.

print(dictionary.update({'z': 'added in'}))  # None - nothing gets returned
print(dictionary)  # update will add in a key:value if key didn't exist.
