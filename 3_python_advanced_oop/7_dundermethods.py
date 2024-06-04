# dunder methods -
# methods that start and end with double underscore.
#

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

# special case when you overwrite a dunder method, this only modifies the behaviour for instances of the Toy class. So __str__ or str() works as expected for anything else.
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return ('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
# this and the below are exactly the same result
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))

print(action_figure())  # yes??
print(action_figure['name'])  # yoyo


# exercise create a super list

# by adding list in, SuperList inherits from the list class similar to how we did Wizard(User) to inherit from User class
class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))  # 1000

super_list1.append(5)
print(super_list1[0])  # 5
print(issubclass(SuperList, list))  # True
print(issubclass(list, object))  # True
