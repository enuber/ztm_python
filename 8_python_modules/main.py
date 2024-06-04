# import utility
import shopping.shopping_cart as cart
# import shopping.more_shopping.more_shopping as cart2

# can do this and then use more_shopping.buy_this to access the function you may do this so that there is no name colision. Like two functions with same name. So would be good to know where things are coming from.
# from shopping.more_shopping import more_shopping

# can do this instead of above and now just use buy_this as if the function were apart of this file.
from shopping.more_shopping.more_shopping import buy_this
from utility import multiply, divide

# print(utility)  # gives you just the <module 'utility' from ...>

# print(utility.divide(5, 4))  # 1.25

# print(more_shopping.buy_this('eggs')) # eggs

print(cart.buy('apple'))  # ['apple']

print(buy_this('orange'))  # ['orange']

print(multiply(5, 2))  # 10


if __name__ == '__main__':
    print('please run this')
