# TESTING
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/unittest.html#assert-methods

# this is the testing package that comes with python
import unittest
# file that we will be testing
from main import do_stuff

# standard way to do this is make a test class with all the functions that we want to run inside of it.


class TestMain(unittest.TestCase):

    # this setup will be called before each function runs. can do whatever you need to set things up.
    def setUp(self):
        print('about to test a function')

    # function to test the do_stuff funciton from main
    def test_do_stuff(self):
        # a test parameter to run
        test_param = 10
        # calling the function to get the result
        result = do_stuff(test_param)
        # this is where we are using part of unittest to assert what we expect to get back first we pass it the result of running the function and second is what it should be
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        # will throw error because it's a string but we are testing that to have happen
        test_param = 'what'
        result = do_stuff(test_param)
        # there are different types of asserts put a link at top of file to see the list
        self.assertEqual(result, 'please enter a valid number')

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter a valid number')

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter a valid number')

    def test_do_stuff5(self):
        test_param = 0
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

# this happens after each function is called where you can clean things up. This isn't used as often.
    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()


# as typically doing unit testing on multiple modules,
# to do this we use the following line in the terminal
# python3 -m unittest

# this command gives more info with it telling you more explicitly what passed or not.
# python3 -m unittest -v
