# Under the hood

# this is how a for loop works. It takes in an iterable and goes through it for each piece of data and then stops.
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            # gives us the actual value in our case 1, 2, 3 individually as it grabs each item in the iterable
            print(next(iterator))
        except StopIteration:
            break


# gives us back the <list_iterator object at space_in_memory> 4 times. but its the same space in memory it's accessing
special_for([1, 2, 3])


# for range...

class MyGen():

    current = 0

    def __init__(self, first, last):
        self.fist = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)  # gives us 0 through 99 as expected


# EXERCSISE FIBONACCI

def fib(number):
    num1 = 0
    num2 = 1
    for i in range(number):
        # remember that yield pauses here so in the loop below that calls this function, we will get each number back and then will do the next three lines of code.
        yield num1
        temp = num1
        num1 = num2
        num2 = temp + num2


def fib2(number):
    num1 = 0
    num2 = 1
    result = []
    for i in range(number):
        result.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return result


for x in fib(21):
    print(x)

print(fib2(21))
