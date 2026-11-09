import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(97))

    def test_composite_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))

    def test_edge_cases(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-2))

    def test_non_integer_input(self):
        self.assertFalse(is_prime(3.5))
        self.assertFalse(is_prime("string"))

if __name__ == "__main__":
    unittest.main()