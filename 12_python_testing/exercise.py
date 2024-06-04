from random import randint


def run_guess(guess, answer):
    if int(guess) == int(answer):
        print('you guessed correctly')
        return True
    elif int(answer) < int(guess):
        print('your guess was to high')
    elif int(answer) > int(guess):
        print('your guess was to low')
    else:
        print('you need to choose a number between 1-10')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    print(answer)

    while True:
        guess = input('guess a number 1-10:  ')
        try:
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
