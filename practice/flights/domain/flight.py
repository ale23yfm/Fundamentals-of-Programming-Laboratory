class Flight:
    def __init__(self, flight_id, d_city, d_time_str, a_city, a_time_str):
        self.flight_id = flight_id
        self.a_city = a_city
        self.a_time_str = a_time_str
        self.d_city = d_city
        self.d_time_str = d_time_str

        self.a_time_min = self._time_to_minutes(a_time_str)
        self.d_time_min = self._time_to_minutes(d_time_str)

    def _time_to_minutes(self, time_str: str) -> int:  # instance method
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    @property
    def duration(self):
        return self.a_time_min - self.d_time_min

    @property
    def id(self):
        return self.flight_id

    def __str__(self):
        return f"{self.d_time_str} | {self.a_time_str} | {self.flight_id} | {self.d_city} - {self.a_city}"
