
# multiple inheritance - allows you to inherit from mulitple classes.

class User():

    def sign_in(self):
        print('logged in')


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'arrows left {self.num_arrows}')

    def run(self):
        print('ran really fast')


class Hybrid(Wizard, Archer):

    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
hybrid1 = Hybrid('Hy', 50, 100)

hybrid1.run()  # ran really fast
hybrid1.attack()  # attacking with power of 50
hybrid1.check_arrows()  # arrows left 100
hybrid1.sign_in()  # logged in


# METHOD RESOLUTION ORDER

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # 1 because MRO is D then B then C then A and even though C inherits from A it's "num" is defined so becomes the num due to order of MRO. it's like having attack in wizard and user, if we did wizard1.attack() the method in wizard is run not in user. This is the same thing. But it is this way for a reason
print(D.mro())  # will give list of MRO so you understand the order.
