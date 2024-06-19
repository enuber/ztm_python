# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.

from bs4 import BeautifulSoup
import requests
import random


def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]
    return stages[incorrect_guesses]


def get_words():
    base_URL = 'https://norvig.com/ngrams/sowpods.txt'

    res = requests.get(base_URL)
    soup = BeautifulSoup(res.text, 'html.parser')

    with open('words.txt', mode='w') as file:
        for word in soup:
            file.write(word + '\n')


def random_word():
    with open('words.txt', mode='r') as file:
        word_list = [word.strip() for word in file if len(word) > 4]
    return random.choice(word_list).upper()


def check_letter(guess, word_to_guess, current_state_of_word):
    letter_locations = [idx for idx, letter in enumerate(
        word_to_guess) if guess == letter]
    for idx in letter_locations:
        current_state_of_word[idx] = guess
    return current_state_of_word


def final_message(incorrect_guesses, word_to_guess):
    if incorrect_guesses == 0:
        print(f'You lost, the word was {word_to_guess}')
    else:
        print(f'Congratulations! You guessed the word: {word_to_guess}')


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word_to_guess = random_word()
    print(word_to_guess)
    current_state_of_word = ['_' for _ in range(len(word_to_guess))]
    letters_guessed = []
    incorrect_guesses = 6
    print('Welcome to Hangman ! ')
    print(' '.join(current_state_of_word), '\n')
    print(display_hangman(incorrect_guesses))
    while '_' in current_state_of_word and incorrect_guesses > 0:
        try:
            guess = input('Guess a letter :  ').strip().upper()
            if (guess in letters_guessed):
                raise ValueError('This letter has already been guessed.')
            if (guess not in alphabet):
                raise ValueError('Please guess a valid letter.')
        except ValueError as e:
            print(e)
        else:
            letters_guessed.append(guess)
            if guess not in word_to_guess:
                incorrect_guesses -= 1
                print(f'\nThe letter {guess} was not in the word, you have {
                      incorrect_guesses} left \n')
            else:
                current_state_of_word = check_letter(
                    guess, word_to_guess, current_state_of_word)
            print(' '.join(current_state_of_word), '\n')
            print(display_hangman(incorrect_guesses))

    final_message(incorrect_guesses, word_to_guess)
    while True:
        answers = ['y', 'n', 'yes', 'no']
        try:
            restart = input(
                '\nWould you like to start a new game (Y/N)? ').strip().lower()
            if restart not in answers:
                raise ValueError('Please try again.')
        except ValueError as e:
            print(e)
        else:
            if restart in ['y', 'yes']:
                main()
            else:
                break


if __name__ == "__main__":
    # get_words() # this will grab the file and create it if you don't already have it.
    main()
