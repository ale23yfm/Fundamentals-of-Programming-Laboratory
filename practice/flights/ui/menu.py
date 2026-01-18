from ..errors.errors import ServiceError, RepositoryError
from ..repository.text_file_repo import TextFileRepository
from ..service.flight_service import FlightService
from ..domain.flight import Flight

repo = TextFileRepository("flights.txt")
service = FlightService(repo)

class Console():
    print ("Welcome to the console. Type 'help' to see the commands.")
    while True:
        o = input(" >>>   ").strip()
        if not o:
            continue
        parts = o.split()
        cmd = parts[0].lower()

        if cmd == "help":
            print ("Available commands: \n"
                   "help\n"
                   "add <flight_id> <departure_city> <departure_time like HH:MM> <arrival_city> <arrival_time like HH:MM>\n"
                   "delete <flight_id>\n"
                   "list-airports\n"
                   "list-time\n"
                   "list-flights\n"
                   "list\n"
                   "exit")
            continue

        elif cmd == "add":
            if len(parts) < 6:
                print ("Invalid number of arguments. Please enter a flight ID.")
                continue

            try:
                flight_id = parts[1]
                d_city = parts[2]
                d_time = parts[3]
                a_city = parts[4]
                a_time = parts[5]
                flight = Flight(flight_id, d_city, d_time, a_city, a_time)
                service.add_flight(flight)
                print ("Added flight " + flight_id)
            except (ServiceError, RepositoryError, ValueError) as e:
                print(f"Error: {e}")

        elif cmd == "delete":
            if len(parts) < 2:
                print("Usage: delete <id>")
                continue
            flight_id = parts[1]
            try:
                service.delete_flight(flight_id)
                print ("Deleted flight " + flight_id)
            except (ServiceError, RepositoryError, ValueError) as e:
                print(f"Error: {e}")

        elif cmd == "list-airports":
            pass

        elif cmd == "list-time":
            pass

        elif cmd == "list-flights":
            pass

        elif cmd == "list":
            flights = service.get_all_flights()
            if not flights:
                print("No flights in the file.")
            else:
                for f in flights:
                    print(f)
            continue

        elif cmd == "exit":
            print ("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help'.")





