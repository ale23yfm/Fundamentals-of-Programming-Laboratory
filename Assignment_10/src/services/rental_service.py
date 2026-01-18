from collections import Counter, defaultdict

from src.domain import book
from src.domain.rental import Rental
from src.errors.errors import RentalError
from src.services.undo import FunctionCall, Operation


class RentalService:
    def __init__(self, repo, book_service, client_service, undo_service=None):
        self.__repo = repo
        self.__book_service = book_service
        self.__client_service = client_service
        self.__undo_service = undo_service

    def _get_next_id(self):
        rentals = self.__repo.get_all()
        if not rentals:
            return 1
        return max(r.rental_id for r in rentals) + 1

    def get_all(self):
        """
        Function that displays all rented books
        :return: the books
        """
        return self.__repo.get_all()

    def _set_rented(self, rental_id, value: bool):
        """
        Function to set is_rented of a rental (used for undo/redo)
        """
        rental = self.__repo.find_by_id(rental_id)
        if rental:
            rental.is_rented = value

    def rent_book(self, book_id, client_id, days):
        """
        Function that rents a book
        :param book_id: book's id
        :param client_id: client's id
        :param days: number of days to rent
        :return: the rental id for that book
        """
        books = self.__book_service.get_all()
        if not any(b.book_id == book_id for b in books):
            raise RentalError("Book doesn't exist!")

        clients = self.__client_service.get_all()
        if not any(c.client_id == client_id for c in clients):
            raise RentalError("Client doesn't exist!")

        for r in self.__repo.get_all():
            if r.book_id == book_id:
                if r.is_rented == True:
                    raise RentalError("Book already rented!")

        next_id = self._get_next_id()
        rental = Rental(next_id, book_id, client_id, is_rented=True, days=days)
        self.__repo.add(rental)

        if self.__undo_service:
            undo = FunctionCall(self.__repo.remove, rental)
            redo = FunctionCall(self.__repo.add, rental)
            op = Operation(undo, redo)
            self.__undo_service.record(op)
        return rental.rental_id

    def return_book(self, rental_id):
        """
        Function that returns book
        :param rental_id: id of the rental
        """
        rental = self.__repo.find_by_id(rental_id)
        if rental == None:
            raise RentalError("Rental ID not found!")
        if not rental.is_rented:
            raise RentalError("Book returned!")

        if self.__undo_service:
            undo = FunctionCall(self._set_rented, rental_id, True)
            redo = FunctionCall(self._set_rented, rental_id, False)
            op = Operation(undo, redo)
            self.__undo_service.record(op)
        rental.is_rented = False

    def most_rented_books(self):
        """
        Function that returns the most rented books
        :return: the books sorted descendingly by the number of rentals
        """
        rentals = self.__repo.get_all()
        book_ids = [r.book_id for r in rentals]

        counts = Counter(book_ids)
        sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_books

    def most_active_clients(self):
        """
        Function that returns the most active clients according to its days of renting
        :return: the clients sorted descendingly by the number of rental days
        """
        rentals = self.__repo.get_all()
        client_days = defaultdict(int)
        for r in rentals:
            client_days[r.client_id] += r.days
        sorted_clients = sorted(client_days.items(), key=lambda x: x[1], reverse=True)
        return sorted_clients

    def most_rented_author(self):
        """
        Function that returns the most rented author
        :return: the authors sorted descendingly by the number of rentals
        """
        rentals = self.__repo.get_all()
        books = self.__book_service.get_all()
        book_to_author = {}
        authors = []
        for b in books:
            book_to_author[b.book_id] = b.author
        for r in rentals:
            author = book_to_author.get(r.book_id)
            if author:
                authors.append(author)
        counts = Counter(authors)
        sorted_authors = counts.most_common()
        return sorted_authors