from practice.train.errors.errors import TextFileError
from practice.train.domain.train import Route


class TextFileRepo:
    def __init__(self, filepath):
        self._filepath = filepath
        self._hourly_rate = None
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
            if len(parts) == 1:
                self._hourly_rate = parts[0]
                continue
            id = int(parts[0])
            d_city = parts[1]
            d_time = parts[2]
            a_city = parts[3]
            a_time = parts[4]
            tickets = parts[5]

            train = Route(id, d_city, d_time, a_city, a_time, tickets)
            self._train[id] = train

    def save_to_file(self):
        with open(self._filepath, "w") as f:
            f.write(self._hourly_rate+"\n")
            for train in self._train.values():
                f.write(f"{train._id}, {train._d_city}, {train._d_time_str}, {train._a_city}, {train._a_time_str}, {train._tickets}\n")

    def get_all(self):
        return list(self._train.values())

    def get_route(self, route_id):
        route_id = int(route_id)
        if route_id not in self._train:
            raise TextFileError ("Route does not exist.")
        return self._train[route_id]

    def add_route(self, route: Route):
        if route.id in self._train:
            raise TextFileError ("Route id already exists.")
        self._train[route.id] = route
        self.save_to_file()

    @property
    def train(self):
        return self._train

    @property
    def get_hourly_rate(self):
        return self._hourly_rate