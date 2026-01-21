import unittest
from ex import function

class Tests(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(function(2))
        self.assertTrue(function(5))

    def test_not_prime(self):
        self.assertFalse(function(4))
        self.assertFalse(function(8))
