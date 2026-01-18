from .repository.text_file_repo import TextFileRepository
from .service.flight_service import FlightService
from .ui.menu import Console

def main():
    repo = TextFileRepository("flights.txt")
    service = FlightService(repo)
    console = Console(service)
    console.run()

if __name__ == "__main__":
    main()
