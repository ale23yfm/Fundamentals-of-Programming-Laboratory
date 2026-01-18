from src.errors.errors import RentalError


class Rental:
    def __init__(self, rental_id, book_id, client_id, is_rented=False, days=None):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__is_rented = is_rented
        self.__days = days

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def client_id(self):
        return self.__client_id

    @property
    def is_rented(self):
        return self.__is_rented

    @property
    def days(self):
        return self.__days

    @is_rented.setter
    def is_rented(self, value):
        if not isinstance(value, bool):
            raise RentalError("is_rented must be bool")
        self.__is_rented = value

    def rent(self):
        if self.__is_rented:
            raise RentalError("Book already rented!")
        self.__is_rented = True

    def return_book(self):
        if not self.__is_rented:
            raise RentalError("Book is not rented!")
        self.__is_rented = False

    def __str__(self):
        return f"Rental ID: {self.__rental_id}, Book ID: {self.__book_id}, Client ID: {self.__client_id}, Rented: {self.__is_rented}, Days: {self.__days}"

    @classmethod
    def from_line(cls, line: str):
        parts = line.strip().split("|")
        return cls(int(parts[0]), int(parts[1]), int(parts[2]), parts[3] == "True", int(parts[4]))

    def to_line(self) -> str:
        return f"{self.rental_id}|{self.book_id}|{self.client_id}|{self.is_rented}|{self.days}"