from practice.train.domain.train import Route
from practice.train.repository.text_file import TextFileRepo


class RouteService:
    def __init__(self, repo: TextFileRepo):
        self._repo = repo
        self._income = 0.00

    def add_route(self, id, d_city, d_time, a_city, a_time, tickets):
        id = int(id)
        tickets = int(tickets)

        if id in self._repo.train:
            raise ValueError("Id already exists.")

        if d_city == a_city:
            raise ValueError ("Arrival and departure cities may not be the same.")

        if tickets <= 0:
            raise ValueError("There must be at least one ticket.")

        route = Route(id, d_city, d_time, a_city, a_time, tickets)

        if route._d_time_min >= route._a_time_min:
            raise ValueError ("Arrival time must be bigger than departure time.")
        self._repo.add_route(route)

    def get_price(self, route_id):
        route = self._repo.get_route(route_id)
        time_min = route._a_time_min - route._d_time_min
        rate = int(self._repo.get_hourly_rate)
        time = (time_min/60)
        return rate * time

    def sell_ticket(self, route_id):
        route = self._repo.get_route(route_id)
        if route._tickets <= 0:
            raise ValueError ("There are no available tickets.")

        price = self.get_price(route_id)
        route._tickets = route._tickets - 1
        self._repo.save_to_file()

        self._income += price
        return price

    def report(self):
        route = self._repo.get_all()
        return sorted(route, key=lambda r:r.tickets_sold(), reverse = True)

    def get_all(self):
        return self._repo.get_all()

    def get_income(self):
        return self._income