from pathlib import Path

from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from errors.errors import BookError, ValidationError, ClientError, RentalError
from repository.in_memory_repo import InMemoryRepository
from repository.binary_file_repo import BinaryFileRepository
from repository.text_file_repo import TextFileRepository
from services.client_service import ClientService
from services.rental_service import RentalService
from services.book_service import BookService
from ui.menu import Menu
from validation.book_validator import BookValidator
from validation.client_validator import ClientValidator
from initializer.initializer import generate_books, generate_clients, generate_rentals


def read_settings(file_path="settings.properties"):
    path = Path(__file__).parent / file_path
    settings = {}
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=")
                settings[key.strip()] = value.strip()
    return settings

if __name__ == "__main__":
    settings = read_settings()
    repo_type = settings.get("repository", "inmemory")
    books_file = settings.get("books", "")
    clients_file = settings.get("clients", "")
    rentals_file = settings.get("rentals", "")

    if repo_type == "inmemory":
        book_repo = InMemoryRepository()
        client_repo = InMemoryRepository()
        rental_repo = InMemoryRepository()
    elif repo_type == "textfiles":
        book_repo = TextFileRepository(books_file, Book)
        client_repo = TextFileRepository(clients_file, Client)
        rental_repo = TextFileRepository(rentals_file, Rental)
    elif repo_type == "binaryfiles":
        book_repo = BinaryFileRepository(books_file)
        client_repo = BinaryFileRepository(clients_file)
        rental_repo = BinaryFileRepository(rentals_file)

    book_validator = BookValidator()
    book_service = BookService(book_repo, book_validator)

    client_validator = ClientValidator()
    client_service = ClientService(client_repo, client_validator)

    rental_service = RentalService(rental_repo, book_service, client_service)

    books = book_repo.get_all()
    clients = client_repo.get_all()
    rentals = rental_repo.get_all()

    if not books:
        books = generate_books()
        for b in books:
            try:
                book_service.add_book(b.book_id, b.title, b.author)
            except (BookError, ValidationError) as e:
                print(f"Error adding book {b.book_id}: {e}")

    if not clients:
        clients = generate_clients()
        for c in clients:
            try:
                client_service.add_client(c.client_id, c.name)
            except (ClientError, ValidationError) as e:
                print(f"Error adding client {c.client_id}: {e}")

    if not rentals:
        rentals = generate_rentals(books, clients)
        for r in rentals:
            try:
                rental_service.rent_book(r.book_id, r.client_id)
            except (RentalError, ValidationError) as e:
                print(f"Error adding client {r.rental_id}: {e}")

    menu = Menu(book_service, client_service, rental_service)
    menu.menu()
