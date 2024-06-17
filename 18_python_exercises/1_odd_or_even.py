# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = ''
number_to_divide = ''

while True:
    try:
        number = float(input('Please enter a number: '))
    except ValueError:
        print('That is not a valid number, please try again: ')
    else:
        break

while True:
    try:
        number_to_divide = float(
            input('Please enter a number to divide the first by (note: can\'t be 0): '))
        number/number_to_divide
    except ValueError:
        print('Please enter a valid number (can\'t be 0) : ')
    except ZeroDivisionError:
        print('You entered 0, please try another number: ')
    else:
        break

if number % number_to_divide == 0 and number % 2 == 0:
    print(f'Your number, {number} is divisible by {
          number_to_divide} and is even')
elif number % number_to_divide == 0 and number % 2 != 0:
    print(f'Your number, {number} is divisible by {
          number_to_divide} and is odd')
elif number % 2 == 0:
    print(f'Your number, {number} is even')
else:
    print(f'Your number, {number} is odd')
