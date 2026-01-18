from src.domain.book import Book
from src.domain.rental import Rental
from src.errors.errors import BookError
from src.services.undo import FunctionCall, Operation, CascadedOperation


class BookService:
    def __init__(self, repo, validator, undo_service, rental_service=False):
        self.__repo = repo
        self.__validator = validator
        self.__undo_service = undo_service
        self.__rental_service = rental_service

    def get_all(self):
        """
        Function that displays all books
        :return: the books
        """
        return self.__repo.get_all()

    def add_book(self, book_id, title, author):
        """
        Function that adds a book
        :param book_id: book's id
        :param title: book's title
        :param author: book's author
        """
        book = Book(book_id, title, author)
        self.__validator.validate(book)

        #verify if there are any duplicates
        if any(b.book_id == book_id for b in self.__repo.get_all()):
            raise BookError(f'Book with id: {book_id} already exists')

        self.__repo.add(book)

        if self.__undo_service:
            undo = FunctionCall(self.__repo.remove, book)
            redo = FunctionCall(self.__repo.add, book)
            op = Operation(undo, redo)
            self.__undo_service.record(op)

    def remove_book(self, book_id):
        """
        Function that removes a book
        :param book_id: book's id
        :return: 1 if the book exists, 0 otherwise
        """
        for b in self.__repo.get_all():
            if b.book_id == book_id:
                old_book = Book(b.book_id, b.title, b.author)
                affected_rentals = []
                for r in self.__rental_service.get_all():
                    if r.book_id == book_id and r.is_rented == True:
                        old_rental = Rental(r.rental_id, r.book_id, r.client_id, r.is_rented, r.days)
                        r.is_rented = False
                        affected_rentals.append((r, old_rental))

                self.__repo.remove(b)
                if self.__undo_service:
                    cascaded = CascadedOperation()
                    undo_client = FunctionCall(self.add_book, old_book.book_id, old_book.title, old_book.author)
                    redo_client = FunctionCall(self.remove_book, old_book.book_id)
                    cascaded.add(Operation(undo_client, redo_client))

                    for r, old_rental in affected_rentals:
                        undo_rental = FunctionCall(self.__rental_service._set_rented, r.rental_id, True)
                        redo_rental = FunctionCall(self.__rental_service._set_rented, r.rental_id, False)
                        cascaded.add(Operation(undo_rental, redo_rental))

                    self.__undo_service.record(cascaded)
                return 1
        return 0

    def update_book(self, book_id, u_title, u_author):
        """
        Function that updates a book
        :param book_id: book's id
        :param u_title: the new title
        :param u_author: the new author
        :return: 1 if the book exists, 0 otherwise
        """
        for b in self.__repo.get_all():
            if b.book_id == book_id:
                new_book = Book(b.book_id, u_title, u_author)
                old_book = Book(b.book_id, b.title, b.author)
                self.__repo.update(b, new_book)

                if self.__undo_service:
                    undo = FunctionCall(self.__repo.update, new_book, old_book)
                    redo = FunctionCall(self.__repo.update, old_book, new_book)
                    op = Operation(undo, redo)
                    self.__undo_service.record(op)
                return 1
        return 0

    def search_books(self, search_field, search_value):
        """
        Function that searches for books by id, title or author
        :param search_field: id, title or author
        :param search_value: the value to search for
        :return: the found book
        """
        results = []
        search_value = search_value.lower()

        for book in self.__repo.get_all():
            if search_field == "id" and search_value in str(book.book_id).lower():
                results.append(book)
            elif search_field == "title" and search_value in book.title.lower():
                results.append(book)
            elif search_field == "author" and search_value in book.author.lower():
                results.append(book)

        return results