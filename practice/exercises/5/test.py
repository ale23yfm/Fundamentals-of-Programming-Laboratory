import unittest

from ex import no_digits


class Test(unittest.TestCase):
    def test_neg_no(self):
        self.assertEqual(no_digits(-123),3)

    def test_pos_no(self):
        self.assertEqual(no_digits(123),3)

    def test_zero(self):
        self.assertEqual(no_digits(0),1)

    def test_no(self):
        self.assertEqual(no_digits(6),1)