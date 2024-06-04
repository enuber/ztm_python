from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

li = [1, 2, 3, 4, 5, 6, 7]
sentence = "What me worry? - From MAD magazine"

# gives back a dictionary with the total times something appeared in the list, for letters it considers case so M is counted separately from m
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {
    'a': 1,
    'b': 2
})

print(dictionary['a'])  # 1
print(dictionary['c'])  # does not exist


d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)  # True
# if we changed the order of the dict above we would get False, remember a dictionary is unordered by nature, the more in it, the less likely you will get them in order if you print them over and over. This makes them actually be in a specific order... Dictionaries are now ordered as of versiomn 3.7 so this last Class doesn't actually matter unless using earlier version

print(datetime.time(5, 45, 2))  # 05:45:02
print(datetime.date.today())  # will give you todays date

# array is faster then lists

arr = array('i', [1, 2, 3])
print(arr[0])  # 1
