# comprehensions

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)  # [h,e,l,l,o]

# better way with comprehensions
# my_list = [param for param in interable]

# way to look at it create a variable. for each variable in the itterable add it to the list.
li = [char for char in 'really']
print(li)  # [r,e,a,l,l,y]

my_list2 = [num for num in range(0, 100)]

# for each variable in the itterable, before adding it to the list take it and multiply it by 2
my_list3 = [num*2 for num in range(0, 100)]

# expression - num**2, we loop through an itterable and for each of those variables/numbers we put it through the expression and then we have the option to add in a conditional which is the if statement.
# this is neat an all but not so readable so trade off.
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list2)
print(my_list3)
print(my_list4)


# SET Comprehension (only unique items)

li = {char for char in 'really'}
print(li)  # {e, y, a, l, r}

my_list2 = {num for num in range(0, 100)}

my_list3 = {num*2 for num in range(0, 100)}

my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}

print(my_list2)
print(my_list3)
print(my_list4)


# DICT comprehension

simple = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# what we want to do with the data - key:value**2
# then the loop to go through
# then the conditional which finds the values that are even.
my_dict = {key: value**2 for key, value in simple.items() if value % 2 == 0}

print(my_dict)  # {'b':4, 'd':16}

# remember num here is being used for key and value just value is * 2.
my_dict1 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict1)  # {1:2, 2:4, 3:6}


# EXERCISE

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = list(set(x for x in some_list if some_list.count(x) > 1))

# alt way of doing the above since we can create a set to begin with
duplicates = list({x for x in some_list if some_list.count(x) > 1})

print(duplicates)
