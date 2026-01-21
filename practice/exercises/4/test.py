import unittest
from ex import function


class Test(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(function([1,2,3]))

    def test_no_even_number(self):
        self.assertFalse(function([1,3,5]))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            function(None)
