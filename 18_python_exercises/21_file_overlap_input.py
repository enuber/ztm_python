# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)
# https://en.wikipedia.org/wiki/Happy_number

def getinfofromfile(filename):
    return_list = []
    with open(filename, mode='r') as f:
        line = f.readline()
        while line:
            line = int(line.strip())
            return_list.append(line)
            line = f.readline()
    return return_list


li_prime = getinfofromfile('prime_numbers.txt')
li_happy = getinfofromfile('happy_numbers.txt')
overlapping_numbers = []

for num in li_prime:
    if num in li_happy and num not in overlapping_numbers:
        overlapping_numbers.append(num)

print(overlapping_numbers)
