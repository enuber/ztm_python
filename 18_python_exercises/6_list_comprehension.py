# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# one liner
b = [num for num in a if num % 2 == 0]
c = []

# long way
for num in a:
    if num % 2 == 0:
        c.append(num)

print(b)
print(c)


years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# one liner
ages = [2024 - year for year in years_of_birth]

# long way
ages2 = []
for year in years_of_birth:
    ages2.append(2024 - year)

print(ages)
print(ages2)
