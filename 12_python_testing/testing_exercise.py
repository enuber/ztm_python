import unittest
from exercise import run_guess


class TestGame(unittest.TestCase):

    def test_input(self):
        answer = 5
        guess = 5
        result = run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = run_guess(2, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = run_guess(11, 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
