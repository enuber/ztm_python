# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random


def check_guess(guess, answer):
    if (guess == answer):
        return True
    elif (guess > answer):
        print(f'{guess} is to high')
    else:
        print(f'{guess} is to low')
    return False


def play_game():
    while True:
        guesses = 0
        high_num = 10
        number_to_guess = random.randint(1, high_num)

        while True:
            try:
                guess = int(
                    input(f"Guess a number between 1 and {high_num}:  "))
                if guess < 1 or guess > high_num:
                    raise ValueError(
                        'Your number was out of range, try again. ')
                guesses += 1
                found_num = check_guess(guess, number_to_guess)
                if (found_num):
                    print(f'You got it, the correct number is {
                          number_to_guess}. You found the right number in {guesses} guesses')
                    break
            except ValueError as e:
                print(e)

        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ["no", "n", "exit", "quit"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
