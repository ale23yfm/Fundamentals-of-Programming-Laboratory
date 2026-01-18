import unittest

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.services.rental_service import RentalService
from src.validation.book_validator import BookValidator
from src.validation.client_validator import ClientValidator
from src.repository.in_memory_repo import InMemoryRepository
from src.services.book_service import BookService
from src.services.client_service import ClientService


class UnitTestBook(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()
        self.validator = BookValidator()
        self.service = BookService(self.repo, self.validator)

    def test_add_book(self):
        b = Book(1, "Book1", "Author1")
        self.service.add_book(b.book_id, b.title, b.author)
        all_books = self.service.get_all()
        self.assertEqual(len(all_books), 1)

        self.assertEqual(b.book_id, 1)
        self.assertEqual(b.title, "Book1")
        self.assertEqual(b.author, "Author1")

    def test_remove_book(self):
        b = Book(1, "Book1", "Author1")
        self.service.add_book(b.book_id, b.title, b.author)

        cnt = self.service.remove_book(1)
        self.assertEqual(cnt, 1)

        all_books = self.service.get_all()
        self.assertEqual(len(all_books), 0)

        cnt = self.service.remove_book(1)
        self.assertEqual(cnt, 0)

    def test_update_book(self):
        b = Book(1, "Book1", "Author1")
        self.service.add_book(b.book_id, b.title, b.author)

        cnt = self.service.update_book(1, "new title", "new author")
        self.assertEqual(cnt, 1)

        all_books = self.service.get_all()
        self.assertEqual(all_books[0].title, "new title")
        self.assertEqual(all_books[0].author, "new author")

class UnitTestClient(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()
        self.validator = ClientValidator()
        self.service = ClientService(self.repo, self.validator)

    def test_add_client(self):
        c = Client(1, "John Doe")
        self.service.add_client(c.client_id, c.name)
        all_clients = self.service.get_all()
        self.assertEqual(len(all_clients), 1)

        self.assertEqual(c.client_id, 1)
        self.assertEqual(c.name, "John Doe")

    def test_remove_client(self):
        c = Client(1, "John Doe")
        self.service.add_client(c.client_id, c.name)

        cnt = self.service.remove_client(1)
        self.assertEqual(cnt, 1)

        all_client = self.service.get_all()
        self.assertEqual(len(all_client), 0)

        cnt = self.service.remove_client(1)
        self.assertEqual(cnt, 0)

    def test_update_client(self):
        c = Client(1, "John Doe")
        self.service.add_client(c.client_id, c.name)

        cnt = self.service.update_client(1, "Martha")
        self.assertEqual(cnt, 1)

        all_clients = self.service.get_all()
        self.assertEqual(all_clients[0].name, "Martha")

class UnitTestRental(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()
        self.rental_service = RentalService(self.repo)

    def test_rent_book(self):
        rental_id = self.rental_service.rent_book(1, 101)

        rentals = [r for r in self.repo.get_all() if isinstance(r, Rental)]
        self.assertEqual(len(rentals), 1)
        self.assertEqual(rentals[0].rental_id, rental_id)
        self.assertTrue(rentals[0].is_rented)

    def test_return_book(self):
        rental_id = self.rental_service.rent_book(1, 101)

        self.rental_service.return_book(rental_id)

        rentals = [r for r in self.repo.get_all() if isinstance(r, Rental)]
        self.assertEqual(len(rentals), 1)
        self.assertFalse(rentals[0].is_rented)
