class Route:
    def __init__(self, id, d_city, d_time_str, a_city, a_time_str, tickets):
        self._id = int(id)
        self._d_city = d_city
        self._d_time_str = d_time_str
        self._a_city = a_city
        self._a_time_str = a_time_str
        self._tickets = int(tickets)

        self._initial_tickets = int(tickets)

        self._d_time_min = self.time_to_min(self._d_time_str)
        self._a_time_min = self.time_to_min(self._a_time_str)

    def time_to_min(self, time):
        parts = time.split(":")
        if len(parts) != 2:
            raise ValueError("Invalid input. It must be HH:MM")
        h = int(parts[0])
        m = int(parts[1])
        if not (0 <= h < 24 and 0 <= m < 60):
            raise ValueError("Invalid input.")
        return h*60+m

    def tickets_sold(self):
        return self._initial_tickets - self._tickets

    def __str__(self):
        return (f"{self._id}, {self._d_city}, {self._d_time_str}, {self._a_city}, {self._a_time_str}, {self._tickets}")

    @property
    def id(self):
        return self._id