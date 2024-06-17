# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word_to_check = ''

while True:
    try:
        word_to_check = input('Enter a word: ')
        if len(word_to_check) < 2:
            raise (ValueError('Need to enter a word larger than one letter'))
    except ValueError as e:
        print(e)
    else:
        break
    finally:
        print(word_to_check)


def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


word1 = 'radar'
word2 = 'pyton'
word3 = 'Madam'
word4 = 'racecar'

print(f'{word1} is a palindrome: {is_palindrome(word1)}')
print(f'{word2} is a palindrome: {is_palindrome(word2)}')
print(f'{word3} is a palindrome: {is_palindrome(word3)}')
print(f'{word4} is a palindrome: {is_palindrome(word4)}')
print(f'{word_to_check} is a palindrome: {is_palindrome(word_to_check)}')
