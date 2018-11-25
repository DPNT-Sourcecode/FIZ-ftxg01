import unittest

from lib.solutions.FIZ import fizz_buzz_solution

class TestFiz(unittest.TestCase):
    def test_fiz(self):
        self.assertEqual(fizz_buzz_solution.fizz_buzz(1), "1")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(3), "fizz")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(13), "fizz")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(5), "buzz")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(25), "buzz")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(35), "fizz buzz")
        self.assertEqual(fizz_buzz_solution.fizz_buzz(15), "fizz buzz")

    if __name__ == '__main__':
        unittest.main()
