import unittest
from main import do_stuff


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'what'
        result = do_stuff(test_param)
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


if __name__ == '__main__':
    unittest.main()
