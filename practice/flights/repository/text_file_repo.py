from ..domain.flight import Flight
from ..errors.errors import RepositoryError


class TextFileRepository:
    def __init__(self, filepath):
        self._filepath = filepath
        self._flights = {}
        self._load_from_file()

    def _load_from_file(self):
        """
        Loads text file from filepath
        """
        try:
            with open(self._filepath) as f:
                text = f.readlines()
        except FileNotFoundError:
            return

        for line in text:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            flight_id = parts[0]
            d_city = parts[1]
            d_time = parts[2]
            a_city = parts[3]
            a_time = parts[4]

            flight = Flight(flight_id, d_city, d_time, a_city, a_time)
            self._flights[flight.id] = flight

    def _save_to_file(self):
        """
        Saves text file to filepath
        """
        with open(self._filepath, "w") as f:
            for flight in self._flights.values():
                f.write(f"{flight.id}, {flight.d_city}, {flight.d_time_str}, {flight.a_city}, {flight.a_time_str}\n")

    def add_flight(self, flight):
        """
        Adds flight to the text file
        :param flight: the flight to be added
        """
        self._flights[flight.id] = flight
        self._save_to_file()

    def delete_flight(self, flight_id):
        """
        Deletes a flight from the text file by flight_id
        :param flight_id: flight's id to be deleted
        """
        if flight_id not in self._flights:
            raise RepositoryError(f"Flight with id {flight_id} does not exist")

        del self._flights[flight_id]
        self._save_to_file()

    def get_all_flights(self):
        """
        Gets all flights from the text file
        """
        return list(self._flights.values())

    def get_airports_activity(self):
        """1p: Airports sorted by activity (departures + arrivals) DESC"""
        flights = self._repo.get_all_flights()
        activity = {}

        for f in flights:
            activity[f.d_city] = activity.get(f.d_city, 0) + 1
            activity[f.a_city] = activity.get(f.a_city, 0) + 1

        # sort by activity DESC
        sorted_airports = sorted(activity.items(), key=lambda x: x[1], reverse=True)
        return sorted_airports