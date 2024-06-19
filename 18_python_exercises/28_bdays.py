# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. The interaction should look something like this:

import json

birthdays = {}

with open('birthdays.json', mode='r') as file:
    birthdays = json.load(file)


def add_entry():
    name = input('Who do you want to add to the Birthday Dictionary? ').title()
    date = input(f'When was {name} born? ')
    birthdays[name] = date
    with open('birthdays.json', mode='w') as file:
        json.dump(birthdays, file)
    print(f'{name} was added to the birthday dictionary.')


def find_date():
    while True:
        try:
            name = input('Who\'s birthday do you want to look up? ')
            if name not in birthdays.keys():
                raise KeyError('Name not in list, try again')
        except KeyError as e:
            print(e)
        else:
            break
    print(f'{name}\'s birthday is {birthdays[name]}.')


def list_entries():
    print('The current entries in the birthday dictionary are: \n')
    for name in birthdays.keys():
        print(name)


def main():
    choices = ['quit', 'add', 'find', 'list', 'a', 'q', 'f', 'l']
    while True:
        try:
            what_next = input(
                'What do you want to do next? you can: Add, Find, List, Quit\n').lower()
            if what_next not in choices:
                raise ValueError('Please make your choice again')
        except ValueError as e:
            print(e)
        else:
            if what_next in ['quit', 'q']:
                print('Good Bye')
                break
            elif what_next in ['add', 'a']:
                add_entry()
            elif what_next in ['find', 'f']:
                find_date()
            elif what_next in ['list', 'l']:
                list_entries()


if __name__ == '__main__':
    main()
