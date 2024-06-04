from random import randint
import sys

# to run you need to put the arguments into the file call python3 6_guessinggame.py 1 100

answer = randint(int(sys.argv[1]), int(sys.argv[2]))
print(answer)
while True:
    guess = input('guess a number 1-10:  ')
    try:
        if int(guess) == int(answer):
            print('you guessed correctly')
            break
        elif int(answer) < int(guess):
            print('your guess was to high')
        elif int(answer) > int(guess):
            print('your guess was to low')
        else:
            print('you need to choose a number between 1-10')
    except ValueError:
        print('please enter a number')
