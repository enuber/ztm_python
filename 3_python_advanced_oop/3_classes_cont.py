
class PlayerCharacter:
    membership = True

    def __init__(self, name="annoymous", age=0):
        if (self.membership):
            self.name = name
            self.age = age

    def run(self):
        print(f'{self.name} is running')

# @classmethod is a decorator used to define a method that is bound to the class and not the instance of the class. This means that the method can be called on the class itself, rather than on instances of the class. A class method takes the class itself as its first argument, which is conventionally named cls.
# this means you can call PlayerCharacter.adding_things() or player1.adding_things()
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

# class method
# Takes cls as the first parameter.
# Can modify class state that applies across all instances of the class.
# Can be called on the class itself or on an instance.
    @classmethod
    def making_character(cls, num1, num2):
        return cls('Teddy', num1 + num2)

# static method
# does not have access to the class, Does not take cls or self as the first parameter.
# Behaves like a regular function but belongs to the class's namespace.
# Cannot modify class or instance state directly.
    @staticmethod
    def grunting():
        return "grunt"


player1 = PlayerCharacter("Cindy", 40)
player2 = PlayerCharacter("Tom", 24)

print(player1.adding_things(2, 3))  # 5
# 10 - notice that we aren't instantiating anything, it is because @classmethod is a method on the actual class.
print(PlayerCharacter.adding_things(5, 10))

# can use a class method to instantiate
player3 = PlayerCharacter.making_character(6, 8)
print(player3.name)  # Teddy
print(player3.age)  # 14
print(player3.grunting())

# REVIEW


class NameOfClass():
    class_attribute = 'value'

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        pass

    @staticmethod
    def stc_method(param1, param2):
        pass
