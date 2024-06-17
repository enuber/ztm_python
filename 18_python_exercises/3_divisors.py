# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Discussion
# The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.

# There is an easy way to programmatically create lists of numbers in Python.

# To create a list of numbers from 2 to 10, just use the following code:

#   x = range(2, 11)
# Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. Note that the second number in the range() function is not included in the original list.

# Now that x is a list of numbers, the same for loop can be used with the list:

number = ''

while True:
    try:
        number = int(input('Please enter a number: '))
        if number <= 0:
            raise ValueError('Please enter a number greater than 0')
        # note this will never happen as the int(input()) above will throw, just wanted to show the isinstance and how to check if something is a
        elif isinstance(number, str):
            raise ValueError(
                'Please enter a valid number not a word or letter(s)')
    except ValueError as e:
        print(e)
    else:
        break

list_to_use = range(1, number + 1)

print([num for num in list_to_use if number % num == 0])
