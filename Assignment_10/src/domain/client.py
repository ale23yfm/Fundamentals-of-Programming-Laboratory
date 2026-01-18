from src.errors.errors import ValidationError


class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Id:{self.__client_id}, Name: '{self.__name}'"

    @classmethod
    def from_line(cls, line: str):
        line = line.strip()
        if not line:
            return None
        parts = line.split("|")
        if len(parts) != 2:
            raise ValidationError(f"Line format invalid: {line}")
        return cls(int(parts[0]), parts[1])

    def to_line(self) -> str:
        return f"{self.client_id}|{self.name}"
