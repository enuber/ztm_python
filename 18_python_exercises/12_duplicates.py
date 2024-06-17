# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

names = ["Michele", "Robin", "Sara", "Michele"]


def remove_dupes(li):
    new_list = []
    for item in li:
        if item not in new_list:
            new_list.append(item)
    return new_list


print(remove_dupes(names))


def remove_dupes2(li):
    return (list(set(names)))


print(remove_dupes2(names))
