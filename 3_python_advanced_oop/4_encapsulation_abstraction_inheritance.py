# 4 pillars of OOP

# Encapsulation: binding of data and functions that manipulate that data. Encapsulate into one big object so that we keep everything in a box so other things can interact it with. This is the methods and attributes which is what is done when a class is made.

# Abstraction: hiding of information or abstracting information and getting access to only what is necessary. Everything else is hidden away.

class PlayerCharacter:
    membership = True

    def __init__(self, name="annoymous", age=0):
        if (self.membership):
            self._name = name
            self._age = age

    def run(self):
        print(f'{self.name} is running')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter('andrei', 100)
# this is abstraction we call this method and don't care how it was implemented just that we are able to call the method and something happens.
player1.speak()  # my name is andrei, and i am 100 years old
# same with a tuple
# 2 - we don't care how this is done just that we get a result from it.
print((1, 2, 3, 1).count(1))  # 2


# Private vs public variables

# player1.speak = 'booo'
# player1.name = '!!!'
# the above now overwrites the class this isn't good. In python there is no true private variable or methods. We use underscore for what you shouldn't touch. It still can be but it is a standard.


# Inheritence - allows new objects to take on properties of existing objects. So you can inherit classes.
# below is example of inheritence User is main class and wizard/archer are the subclasses that inherit from User.

class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        # way to get attack method in user class to run have to pass self in
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

wizard1.sign_in()  # logged in
wizard1.attack()  # do nothing / attacking with power of 50
archer1.sign_in()  # logged in
archer1.attack()  # attacking with arrows: arrows left 1000

# isinstance(instance, Class) - can use isinstance to find out if something is an instance
# along with User and Wizard it is also an instance of object as object gives all the dunder methods so wizard1 and archer1 have a bunch of other methods that automatically come with them.
print(isinstance(wizard1, User))  # True
print(isinstance(wizard1, Wizard))  # True


# Polymorphism - many forms. Methods belong to objects. In python refers to the way in which object classes can share the same method names but they can behave differently based on what calls them.

# example from previous class example "attack" this method is in two different classes and does two different things.

# this shows polymorphism as we are using one function that takes the instance object and calls attack() method which uses two different classes.
def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
