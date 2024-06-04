# List - ordered sequence of objects of any type

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = ['a', 1, True]

# Data Structure
# way to oragnize data into a folder or some way that holds information, a containter around your data

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
# notebooks <-- list is zero based where first item starts at 0.
print(amazon_cart[0])

# List Slicing
print(amazon_cart)  # gives entire list
# remeber [start:end:stepover]
print(amazon_cart[0::2])  # ['notebooks', 'toys']

# lists are mutable
amazon_cart[0] = 'laptop'

# ['sunglasses', 'toys'] <--- note that slicing gives a new list, so if you assigned it to a variable it is now a separated list and that list can be mutated without mutating the original list.
print(amazon_cart[1:3])
print(amazon_cart)  # will now include laptop instead of notebooks

new_cart = amazon_cart
new_cart[-1] = 'apples'
print(new_cart)
print(amazon_cart)  # note that by doing this, it changes both lists because new_cart is pointing to the same place in memory as amazon_cart so making changes to one updates the same place in memory

new_cart = amazon_cart[:]  # note can use .copy() instead of [:]
new_cart[-1] = 'oranges'
print(new_cart)
# this now properly shows just new_cart updated as we "sliced" amazon cart thereby creating a new place in memory.
print(amazon_cart)


# Matrix
# a way to describe multi-dimensional lists (a list in a list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0][1])  # 2 <--- will grab what is at index 0 which is the list [1,2,3] then the second index number says we look into that list and grab what is at index 1 which is 2

# List Methods

basket = [1, 2, 3, 4, 5]
print(len(basket))  # 5 length

# add to end of list
new_list = basket.append(6)
# None <-- basket.append() doesn't return anything, it changes the list in place. It doesn't produce a value or result.
print(new_list)
print(basket.append(7))  # None same reason as above
basket.append(8)
# [1,2,3,4,5,6,7,8] <-- we can see that the two appends above still placed the items into the list.
print(basket)

# allows you to specify the index to place somthing and then what to place.
basket.insert(3, 3.5)
print(basket)  # [1,2,3,3.5,4,5,6,7,8]

basket.extend([9, 10, 11])  # just adds a list to the first list
print(basket)  # [1,2,3,3.5,4,5,6,7,8,9,10,11]

# removing from list
basket.pop()  # removes last item from list note that pop returns what was removed
print(basket)  # [1,2,3,3.5,4,5,6,7,8,9,10]
basket.pop(3)  # removes item at index of 3
print(basket)  # [1,2,3,4,5,6,7,8,9,10]
basket.remove(10)  # give value to be removed, removes in place
print(basket)  # [1,2,3,4,5,6,7,8,9]
# basket.clear() # removes everything from list
# print(basket) # []

# List methods 2
print(basket.index(2))  # 1 <--gives back the index of where 2 is located
# print(basket.index(7, 0, 2)) # error <-- optional to add in but the 0 here is the index to start looking and the 2 is the index to stop looking. Gives error because 7 isn't found.

print(10 in basket)  # False because 10 isn't found in the basket
print(2 in basket)  # True

print(basket.count(2))  # 1 because the number 2 is only in the basket once.

# List Methods 3
basket.append(3.5)
# basket.sort() # would sort the list
print(basket)  # [1,2,3,3.5,4,5,6,7,8,9] <-- based on above line being run
# [1,2,3,3.5,4,5,6,7,8,9] .sort is a method and doesn't return anything does in place. sorted() is a function and returns the sorted basket as a new array so will print out as expected
print(sorted(basket))
# [1,2,3,4,5,6,7,8,9, 3.5] <--- sorted returned a new array didn't actually mutate this array.
print(basket)
basket.reverse()
print(basket)  # [3.5,9,8,7,6,5,4,3,2,1]

# common list patterns
# [1,2,3,4,5,6,7,8,9, 3.5] uses slice to reverse the list again so it's back to how it was.
print(basket[::-1])
# .reverse() mutated the list basket[::-1] creates new list does not mutate the original list.
print(basket)

print(list(range(1, 100)))  # will create a list holding values from 1 to 99
print(list(range(101)))  # will create a list from 0 to 100

sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JoJo'])
print(new_sentence)  # joins a list together with whatever is in the '' like in sentence it is an empty space, could be though a ', ' comma with a space after
# this is the more common practice below with not using a seperate variable
new_sentence1 = ' '.join(['hi', 'my', 'name', 'is', 'JoJo'])
print(new_sentence1)

# list unpacking

a, b, c = [1, 2, 3]
print(a)  # 1
print(b)  # 2
print(c)  # 3

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7]
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(other)  # [4,5,6]
print(d)  # 7
