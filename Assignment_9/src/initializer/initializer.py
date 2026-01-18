import random

from faker import Faker
from domain.book import Book
from domain.client import Client
from domain.rental import Rental

fake = Faker()

def generate_books(n=25):
    books = []
    for i in range(1, n + 1):
        book_id = i
        title = fake.sentence(nb_words=3).replace("|", " ")
        author = fake.name().replace("|", " ")
        books.append(Book(book_id, title, author))
    return books

def generate_clients(n=25):
    clients = []
    for i in range(1, n + 1):
        client_id = i
        name = fake.name().replace("|", " ")
        clients.append(Client(client_id, name))
    return clients

def generate_rentals(books, clients, n=20):
    rentals = []
    books_to_rent = random.sample(books, n)

    for rental_id, book in enumerate(books_to_rent, start=1):
        client = random.choice(clients)
        rental = Rental(rental_id, book.book_id, client.client_id)
        rentals.append(rental)

    return rentals

