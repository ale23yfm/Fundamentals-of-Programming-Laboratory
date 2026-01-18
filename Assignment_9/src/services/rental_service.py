from domain import book
from domain.rental import Rental
from errors.errors import RentalError


class RentalService:
    def __init__(self, repo, book_service, client_service):
        self.__repo = repo
        self.__book_service = book_service
        self.__client_service = client_service

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

    def rent_book(self, book_id, client_id):
        """
        Function that rents a book
        :param book_id: book's id
        :param client_id: client's id
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
        rental = Rental(next_id, book_id, client_id, is_rented=True)
        self.__repo.add(rental)
        return rental.rental_id

    def test_return_book(self):
        # arrange
        self.book_service.add_book(1, "Book1", "Author1")
        self.client_service.add_client(101, "John Doe")

        rental_id = self.rental_service.rent_book(1, 101)

        # act
        self.rental_service.return_book(rental_id)

        # assert
        rentals = self.repo.get_all()
        self.assertEqual(len(rentals), 1)
        self.assertFalse(rentals[0].is_rented)


