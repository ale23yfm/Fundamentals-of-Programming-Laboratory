import unittest

from ex import sum_even

class Tests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_even([1, 2, 3]), 2)

    def test_not_sum(self):
        self.assertNotEqual(sum_even([1,2,3]), 4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            sum_even("not a list")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            sum_even([1,3])

