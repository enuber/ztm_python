# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

def play_game():
    print("Think of a number between 1 and 100 and I will try to guess it")
    low = 0
    high = 100
    guesses = 0

    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        print(f"My guess is: {guess}")
        while True:
            try:
                feedback = input(
                    "Enter 'h' if my guess was to high, 'l' if it is to low, or 'c' if it is correct: ").lower()
                if feedback not in ['h', 'l', 'c']:
                    raise ValueError("please enter the correct information")
            except ValueError as e:
                print(e)
            else:
                break

        if feedback == 'c':
            print(f"I guessed your number {guess} in {guesses} guesses")
            break
        elif feedback == 'h':
            high = guess - 1
        else:
            low = guess + 1


if __name__ == "__main__":
    play_game()
