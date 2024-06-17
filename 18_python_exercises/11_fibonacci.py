# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def generate_fibonacci(n):
    """
    Generate a list of the first n Fibonacci numbers.
    """
    # should never hit this because of the check in the main function but adding this for reuseability and/or if the function is called directly wtihout getting info from the user.
    if n <= 0:
        return []

    # fibonacci starts with a 1 so starting the list with that in it.
    fibonacci_sequence = [1]

    if n > 1:
        fibonacci_sequence.append(1)
        for i in range(2, n):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

    return fibonacci_sequence


def main():
    """
    Main function to interact with the user and display the Fibonacci sequence.
    """
    while True:
        try:
            num = int(
                input('How many Fibonacci numbers would you like to generate? '))
            if num <= 0:
                raise ValueError('Please enter a number greater than 0.')
        except ValueError as e:
            print(e)
        else:
            break

    fibonacci_sequence = generate_fibonacci(num)
    print(f'The first {num} Fibonacci numbers are:')
    print(fibonacci_sequence)


if __name__ == '__main__':
    main()
