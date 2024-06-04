birth_year = input("What year were you born? ")

age = 2024 - int(birth_year)

print(f'your age is: {age}')

# DEVELOPER FUNDAMENTAL
"""
commenting code can use # in front of line to comment it out
can use triple quotes for multi-line comment

"""

# https://realpython.com/python-comments-guide/

# next exercise
user_name = input('What is your username? ')
password = input('what is your password? ')
password_length = len(password);
hidden_password = '*' * password_length;

print(f'{user_name}, your password {hidden_password} is {password_length} letters long')