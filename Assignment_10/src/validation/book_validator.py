from configobj.validate import is_integer

from src.errors.errors import ValidationError


class BookValidator:
    @staticmethod
    def validate(book):
        error =[]
        if book.book_id < 0 or not(is_integer(book.book_id)):
            error.append("Book ID is invalid. It must be a positive integer.")
        if len(book.title.strip()) == 0:
            error.append("Title cannot be empty")
        if len(book.author.strip()) == 0:
            error.append("Author cannot be empty")

        if error:
            raise ValidationError("\n".join(error))