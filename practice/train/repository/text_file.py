from practice.train.errors.errors import TextFileError
from practice.train.domain.train import Route


class TextFileRepo:
    def __init__(self, filepath):
        self._filepath = filepath
        self._train= {}
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self._filepath, "r") as f:
                text = f.readlines()
        except FileNotFoundError as e:
            raise TextFileError from e

        for line in text:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            id = parts[0]
            d_city = parts[1]
            d_time = parts[2]
            a_city = parts[3]
            a_time = parts[4]
            tickets = parts[5]

            train = Route(id, d_city, d_time, a_city, a_time, tickets)
            self._train[id] = train

    def save_to_file(self):
        with open(self._filepath, "w") as f:
            for train in self._train.values():
                f.write(f"{train.id}, {train.d_city}, {train.d_time_str}, {train.a_city}, {train.a_time_str}, {train.tickets}")
