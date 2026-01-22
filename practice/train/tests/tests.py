import os
import unittest

from practice.train.repository.text_file import TextFileRepo
from practice.train.service.service import RouteService

TEST_FILE = "test_routes.txt"

class Test(unittest.TestCase):
    def write_file(self, content):
        with open(TEST_FILE, "w") as f:
            f.write(content)

    def setUp(self):
        self.write_file("10\n1,a,2:00,b,3:30,10\n")
        self.repo = TextFileRepo(TEST_FILE)
        self.service = RouteService(self.repo)

    def tearDown(self):
        # runs AFTER every test
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_route(self):
        self.service.add_route(2, "a", "10:00", "b", "12:00", 15)
        self.assertEqual(len(self.repo.get_all()), 2)

    def test_get_price(self):
        self.assertEqual(self.service.get_price(1),15)

    def test_sell_ticket(self):
        self.service.sell_ticket(1)
        self.assertEqual(self.repo.get_route(1)._tickets, 9)

    def test_income(self):
        self.service.sell_ticket(1)
        self.assertEqual(self.service.get_income(), 15)
