# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random


def generate_answer():
    final_answer = []
    for _ in range(4):
        final_answer.append(str(random.randint(0, 9)))
    return ''.join(final_answer)


def show_rules():
    print('Welcome to Cows and Bulls')
    print('You will be asked to guess a four digit number from 0000-9999')
    print('For every digit you guessed correctly and is in the correct place you will get a cow')
    print('For every digit you guess correctly but is in the wrong place you will get a bull')


def correct_guess(guess):
    guess = str(guess)
    if len(guess) < 4:
        guess_list = list(guess)
        for _ in range(4 - len(guess)):
            guess_list.insert(0, '0')
        guess = ''.join(guess_list)
    return guess


def check_guess(guess, solution):
    cows_bulls = [0, 0]  # [cows, bulls]
    guess = correct_guess(guess)
    guess = list(guess)
    solution = list(solution)
    # count cows
    for i in range(4):
        if guess[i] == solution[i]:
            cows_bulls[0] += 1
    # count bulls
    for i in range(4):
        if guess[i] in solution and guess[i] != solution[i]:
            cows_bulls[1] += 1

    return cows_bulls


if __name__ == "__main__":
    solution = generate_answer()
    print(solution)
    guess_attempts = 0
    show_rules()
    while True:
        try:
            guess = int(input('Guess a 4 digit number from 0000-9999 :  '))

            if 0 > guess > 9999:
                raise ValueError(
                    'Your guess is out of range; please try again')
        except ValueError as e:
            print(e)
        else:
            guess_attempts += 1
            cows, bulls = check_guess(guess, solution)
            if cows == 4:
                print(f'you guessed the correct number {
                      solution} in {guess_attempts} turns')
                break
            else:
                print(f'You have {cows} cows and {bulls} bulls')
