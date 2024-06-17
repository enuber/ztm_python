# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

number = ''

while True:
    try:
        number = int(input('Please enter a number: '))
        if number <= 1:
            raise ValueError('Please enter a number greater than 1')
    except ValueError as e:
        print(e)
    else:
        break


def is_prime(number):
    # list_to_use = range(2, number)
    # divisors = []

    # for num in list_to_use:
    #     if number % num == 0:
    #         divisors.append(num)
    # if len(divisors) == 0:
    #     print(f'{number} is prime')
    # else:
    #     print(f'{number} is not prime')

    numbers_list = [num for num in range(2, number) if number % num == 0]
    if len(numbers_list) == 0:
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')


is_prime(number)
