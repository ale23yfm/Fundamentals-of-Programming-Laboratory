import unittest

from ex import sum_even_no


class Test(unittest.TestCase):
    def test_sum(self):
        l = [2, 2, 4, 5, 6, 4, 13, 4, 10]
        self.assertEqual(sum_even_no(l), 22)

    def test_no_number(self):
        l = [1, 4, 5, 6, 13, 4, 11]
        self.assertEqual(sum_even_no(l), 0)

