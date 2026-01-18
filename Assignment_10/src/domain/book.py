from src.errors.errors import ValidationError


class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author

    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Id: {self.__book_id} Title: {self.__title} Author: {self.__author}"

    @classmethod
    def from_line(cls, line: str):
        line = line.strip()
        if not line:
            return None
        parts = line.split("|")
        if len(parts) != 3:
            raise ValidationError(f"Line format invalid: {line}")
        return cls(int(parts[0]), parts[1], parts[2])

    def to_line(self) -> str:
        return f"{self.book_id}|{self.title}|{self.author}"
