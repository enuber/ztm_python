# What is OOP
# allows us to write code that is repeatable, organized and memory efficient.

# everything in python is an object. everything is built using classes. Even datatypes if you use print(type(5)) will come back as <class 'int'>

# as code gets bigger and more complicated - OOP is a paradigm, easier to maintain and extend. You break things down into smaller pieces. Break up functionality so different people can work on different portions of a project and then combine them all at the end. If you then want to build something similar, you can move code over and use some pieces even easier and then add in what makes the new thing different.

# class is a keyword, standard is to use a capital letter for name of class and camelcase instead of snakecase
class BigObject:
    pass


# to use the class to create something we simply call it and assign it to a variable.
obj1 = BigObject()

print(type(obj1))  # __main__.BigObject

# a class is the blueprint of what we want to create, the attributes, properties, methods. then we use that blueprint as the building block to make objects. We use the class by instantiting it which makes instances of it in objects. Above the class is BigObject. The instance is obj1 and we instantiate it by saying BigObject().


# CREATING OUR OWN OBJECTS

class PlayerCharacter:

    # class object attribute - on the same level as the functions below. It isn't dynamic, it is static.
    # it is an actual attribute on this class. It will exist for all objects, doesn't need to be set, it just exists for each object. If it needed to be set it would need to be in the __init__
    membership = True

  # __init__ is a dunder method. It is a constructor method or an init method. Automatically called when we instantiate an object.
  # What is self? - this is a way for us to define self. It refers to the PlayerCharacter and refers to this one.
  # so in our case self refers to player1. It refers to the instance object we are creating. It is basically like saying player1.name but, as this is a class and is a blueprint, we say "self". So that each time a new instance is created the self refers to the instance object being created.
    def __init__(self, name="annoymous", age=0):
        # we can call self or PlayerCharacter.membership because it is a class object attribute. It belongs to the class itself.
        if (self.membership):
            # we are saying this particular version of the object will have the name we passed in. "self" is like saying "This" PlayerCharacter dot name is equal to the name passed in.
            # these are attributes - pieces of data that are dynamic that are unqiue to each object
            self.name = name
            self.age = age

    # these are methods you must pass self in first
    def run(self):
        # have to refer to self.<attributename> in order to use. because we are referring to a specific instantiation of the class. {name} itself won't work as the class then doesn't know what name to use.
        print(f'{self.name} is running')


player1 = PlayerCharacter("Cindy", 40)
player2 = PlayerCharacter("Tom", 24)

# < __main__.PlayerCharacter object at 0x1002415e500> - we created a playercharacter which is an object stored at a specific location in memory. Each player will live at different places in memory.
print(player1)
print(player1.name)  # Cindy
print(player1.age)  # 40
print(player1.run())  # run None - runs the method inside the class. We get None because we aren't returning anything from the function. if you just call player.run() without wrapping in print() we would just get run. Or if we returned something from the run function like return "done" we would get run done
print(player2.age)  # 24

player2.attack = 50

print(player2.attack)  # 50
# print(player1.attack) # gives an error because player1 doesn't have the attack method attached to it. we defined it only for player 2.

# by using help we can get a print out of what is included in a class
# help(player1)
# help(list)
