from domain.book import Book
from errors.errors import BookError


class BookService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

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

    def remove_book(self, book_id):
        """
        Function that removes a book
        :param book_id: book's id
        :return: 1 if the book exists, 0 otherwise
        """
        for b in self.__repo.get_all():
            if b.book_id == book_id:
                self.__repo.remove(b)
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
                book = Book(b.book_id, u_title, u_author)
                self.__repo.update(b, book)
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