# super()
# added in an init to User

# we need to call the init function in the User class from the other classes so that we have access to the email attribute.

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):

    def __init__(self, name, power, email):
        # a way to hook up so that we get access to email in User class. have to pass through email.
        # User.__init__(self, email)
        # more common way is to use super()
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robin@gmail.com')

wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()
print(wizard1.email)

# Introspection - ability to determine the type of an object at runtime.
# use dir(object) to get a list of all the methods and attributes that the ojbect instance has.
print(dir(wizard1))
