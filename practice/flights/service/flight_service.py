from ..domain.flight import Flight
from ..errors.errors import ServiceError


class FlightService:
    def __init__(self, repo):
        self._repo = repo

    def add_flight(self, flight: Flight):
        """
        Adds a flight to the text file
        :param flight: flight to be added
        """
        ids = [f.id for f in self._repo.get_all_flights()]
        if flight.id in ids:
            raise ServiceError("Flight id already exists")

        if not (15 <= flight.duration <= 90):
            raise ServiceError("Flight duration must be between 15 and 90 minutes")

        for f in self._repo.get_all_flights():
            if f.d_city == flight.d_city and f.d_time_min == flight.d_time_min:
                raise ServiceError(f"Departure airport in {flight.d_city} is busy at {flight.d_time_str}")

            if f.a_city == flight.a_city and f.a_time_min == flight.a_time_min:
                raise ServiceError(f"Arrival airport in {flight.a_city} is busy at {flight.a_time_str}")

        self._repo.add_flight(flight)

    def delete_flight(self, flight_id):
        """
        Deletes a flight from the text file
        :param flight_id: flight's id to be deleted
        """
        self._repo.delete_flight(flight_id)

    def get_all_flights(self):
        """
        Gets all flights from the text file
        """
        return self._repo.get_all_flights()
