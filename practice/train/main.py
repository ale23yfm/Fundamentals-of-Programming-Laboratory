from pathlib import Path

from texttable import Texttable

from practice.train.errors.errors import TextFileError
from practice.train.repository.text_file import TextFileRepo
from practice.train.service.service import RouteService


def main(service):
    print("Welcome to the train routes! Type 'help' to find out the commands. Enjoy your journey!")
    while True:
        inp = input(">>>>").strip()
        parts = inp.split(" ")
        cmd = parts[0].lower()

        if cmd == "help":
            print("Available commands:"
                  "help\n"
                  "add <id> <departure city> <departure time HH:MM> <arrival city> <arrival time HH:MM> <tickets>\n"
                  "sell <id>\n"
                  "show\n"
                  "report\n"
                  "exit")

        elif cmd == "exit":
            print("Goodbyeeeeeeeeee!")
            break

        elif cmd == "add":
            if len(parts) != 7:
                print("Invalid number of parameters, try again")
                continue
            try:
                id = int(parts[1])
                d_city = parts[2]
                d_time = parts[3]
                a_city = parts[4]
                a_time = parts[5]
                tickets = parts[6]
                service.add_route(id, d_city, d_time, a_city, a_time, tickets)
                routes = service.get_all()
                print("Instance added successfully:")
                for r in routes:
                    print(r)
            except (ValueError, TextFileError) as e:
                print(f"{e}")
                continue

        elif cmd == "sell":
            if len(parts) != 2:
                print("Invalid number of parameters, try again")
                continue
            try:
                id = int(parts[1])
                answer = input(f"The price of your ticket would be {service.get_price(id)}. Do you want it?(Yes/No)")
                answer.strip().lower()
                if answer == "yes":
                    service.sell_ticket(id)
                    print("Enjoy it!")
                    continue
                else:
                    print("Thank you for your time")
                    continue
            except ValueError as e:
                print(f"{e}")

        elif cmd == "show":
            try:
                print(f"Total income: {service.get_income():.2f}")
            except ValueError as e:
                print(f"{e}")

        elif cmd == "report":
            table = Texttable()
            table.set_cols_align(["c"]*7)
            table.set_cols_valign(["m"]*7)
            report = service.report()
            if not report:
                print("No routes available.")
                continue

            print(f"The report:")
            table.add_row(["ID", "From", "Dep", "To", "Arr", "Left", "Sold"])
            for r in report:
                table.add_row([r.id, r._d_city, r._d_time_str, r._a_city, r._a_time_str, r._tickets, r.tickets_sold()])
            print(table.draw())

        else:
            print("Invalid command, try again.")
            continue


if __name__ == "__main__":
    path = Path(__file__).with_name("routes.txt")
    repo = TextFileRepo(str(path))
    service = RouteService(repo)
    main(service)

    for r in repo.get_all():
        print(r)