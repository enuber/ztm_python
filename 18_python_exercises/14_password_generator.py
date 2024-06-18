# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
size = ''


def password_generator(size=8):
    return ''.join(random.choice(characters) for _ in range(size))


while True:
    try:
        size = int(
            input('How many characters do you want your password to be : '))
        if size < 8:
            raise ValueError(
                'Your password should be at least 8 characters. Try again')
    except ValueError as e:
        print(e)
    else:
        break


print(password_generator(size))
