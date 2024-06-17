# Error Handling

# except block runs if something goes wrong
# for except blocks can give it what type of error to handle so that you can handle different types of errors. If not concerned with multiple errors just leave as except:
# if you have the same types of errors like ValueError multiple times, it will only hit the first error type.
# else will happen if try works. Allows you to do clean up and get out of loop
while True:
    try:
        age = int(input('what is your age?'))
        age/0
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please endter age higher than 0')
    else:
        print('thank you')
        break

#  PART 2


def sum(num1, num2):
    try:
        return num1 + num2
    # using as err: allows you to get access to the error itself.
    except TypeError as err:
        print(f'please enter numbers {err}')
    # below is way to combine multiple types of errors and you can still get access to what the error is and print it.
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum('1', 2))  # please enter numbers


# Exercises: error handling

while True:
    try:
        age = int(input('what is your age?'))
        age/0
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please endter age higher than 0')
    else:
        print('thank you')
        break
    # no matter what this will run whether error or not.
    finally:
        print('ok, i am finally done')

# Part 3

while True:
    try:
        age = int(input('what is your age?'))
        age/0
        # can raise your own value errors this way as well. useful if creating own library or tool.
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    # no matter what this will run whether error or not.
    finally:
        print('ok, i am finally done')
