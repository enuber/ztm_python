# sets
# unordered collections of unique objects

my_set = {1, 2, 3, 4, 5, 3, 2, 1} 
print(my_set) # {1, 2, 3, 4, 5} - removes duplicates

my_list = [1,2,3,4,5,5,5,2]

print(set(my_list)) # {1,2,3,4,5}

#when useful - example usernames or email addresses where we don't want dupes. 

# print(my_set[1]) # gives error, can't use indexing to get data

print(1 in my_set) # True - way to check if something exists in set

print(len(my_set)) # 5 

print(list(my_set)) # [1,2,3,4,5] will convert to a list

new_set = my_set.copy() # will be unique copy of set


my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# 
print(my_set.difference(your_set)) # 1, 2, 3 - looks at two sets and finds what is different in my_set, ie not included in your_set

# my_set.discard(5)
# print(my_set) # {1,2,3,4} - removes something from the set, but doesn't return something so printed on separate line to show it's gone


# my_set.difference_update(your_set) 
# print(my_set) # {1,2,3} - this finds the difference and updates the list, changing it. but again doesn't return somethingon it's own so printing on own line.

print(my_set.intersection(your_set)) # {4,5} - gives us back what is common between two sets

print(my_set.isdisjoint(your_set)) # False - looks to see if there are things in common, if there are no things in common would return true, if they have things in common returns false


my_set.issubset(your_set) # False - looks to see if everything in it is also inside your_set, if it is all in then get True, if there are things not in your_set then get False.


your_set.issuperset(my_set) # False - this is opposite of other it means that, means does your_set contain everything that is in my_set. If so then get True otherwise get False. Doesn't work other way around with my_set.issuperset this would be based on my_set just being {4, 5} with this, your_set contains all of my_set but, my_set doesn't contain everything in your_set. 

print(my_set.union(your_set)) # {1,2,3,4,5,6,7,8,9,10} returns the two sets combined and removes dupes, does't mutate either set
print(my_set | your_set) # shorthand for above using the | pipe character

# .update() will allow you do insert items from one set to another.
# .remove() allows you to remove an item from a set