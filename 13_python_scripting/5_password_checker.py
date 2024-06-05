# Password checker
# will use python3 5_password_checker.py password123 hello hasdfsdf
# basically as many passwords as you want to check and will tell you how many times it was found and feedback on changing password

# have i been pwned website can check passwords and emails
# https://haveibeenpwned.com/

# password generator that gives hash password
# passwordsgenerator.net/sha1-hash-generator/

# we send the first five letters only of the hash password. We will get back a list of passwords that start with that hash which we can then use. This is called k-anonymity, can receive info about us but not know who we are.

import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again'
        )
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # we get the hash and the count because we are splitting at the : first part is the hash and second is the count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {
                  count} times...you should probably change your password')
        else:
            print(f'{password} was NOT found, carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
