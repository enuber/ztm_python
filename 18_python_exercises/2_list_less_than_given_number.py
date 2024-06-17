# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in a:
    if num < 5:
        print(num)

new_list = []

for num in a:
    if num < 5:
        new_list.append(num)

print(new_list)


number_to_use = ''
while True:
    try:
        number_to_use = int(input(
            'Enter a number that will be used to search the list and find anything less than that number: '))
        if number_to_use < 0:
            raise ValueError('The number must be positive.')
    except ValueError as e:
        print(e)
    else:
        break

new_list_2 = []

for num in a:
    if num < number_to_use:
        new_list_2.append(num)

print(new_list_2)
