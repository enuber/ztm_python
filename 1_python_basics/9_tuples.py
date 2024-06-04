# Tuple
# lists that can't be modified.

my_tuple = (1,2,3,4,5)

print(my_tuple[1]) # 2 - will still give you back data via indexing
print(4 in my_tuple) # True 

# so why do we need this...
# if you don't need to change the list, it is safer to use this as a tuple can't be changed. Can't sort, can't reverse. 

user = {
  'name': 'erik',
  'age': 50,
  'greet': 'hello',
  (1,2): 'valid'
}

print(user.items()) # dict_tiems([('name', 'erik'),('age', 50),('greet', 'hello')]) we get here all the key:values but as a list of tuples.

print(user[(1,2)]) # valid - can use tuples as key in dict because it immutible.

new_tuple = my_tuple[1:2]

print(new_tuple) # (2,) - can still slice, this looks weird only because it comes back as one item in the new_tuple

x, y, *other = my_tuple
print(x)
print(y) 

# only two methods count and index

print(my_tuple.count(5)) # 1 tells you how many times 5 appears in the tuple

print(my_tuple.index(5)) # 4 gives you the index where the first value appears

print(len(my_tuple)) # 5 gives the lenght of the tuple.