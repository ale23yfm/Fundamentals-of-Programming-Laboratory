#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#

from typing import List, Dict
from texttable import Texttable

from functions import add_expense, filtered_by_amount, filtered_by_type, undo, valid_types, remove_apartment, remove_apartments_range, remove_type, replace_amount

#A
def read_expenses(expenses: List[Dict], history):
    """
    The function handles the inputs of the expenses.
    """
    while True:
        try:
            apartment = int(input("Type the apartment number: "))
            if apartment < 0:
                print("Invalid input. Please type a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please type a positive integer.")
            continue
    while True:
        try:
            expense_type = input("Please select an expense type from the following list: water, heating, electricity, gas and other:")
            if expense_type not in valid_types:
                raise ValueError("Invalid input. Please select an expense type from the following list: water, heating, electricity, gas and other.")
        except ValueError:
            print("Invalid input. Please select an expense type from the following list: water, heating, electricity, gas and other.")
            continue
        break
    while True:
        try:
            amount = int(input("Please type the amount you want to add: "))
            if amount < 0:
                print("Invalid input. Please type a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please type a positive integer.")
            continue

    add_expense(expenses, history, apartment, expense_type, amount)
    print("\nThe following expense has been added to the list:")
    print(expenses[-1])

#C
def display_expenses(expenses: List[Dict]):
    table = Texttable()
    table.header(["Apartment", "Type", "Amount"])
    for e in expenses:
        table.add_row([e["apartment"], e["type"], e["amount"]])
    print(table.draw())

def display_expenses_by_apartment(expenses: List[Dict], apartment: int):
    table = Texttable()
    table.header(["Apartment", "Type", "Amount"])
    for e in expenses:
        if apartment == e["apartment"]:
            table.add_row([e["apartment"], e["type"], e["amount"]])
    print(table.draw())

def display_filtered_by_amount(expenses: List[Dict]):
    while True:
        try:
            operator = input("Type the filter type(choose from <, =, >: ")
            if operator != "<" and operator != "=" and operator != ">":
                print("Invalid input. Please type <, = or >.")
                continue
            break
        except ValueError:
            print("Invalid input. Please type <, = or >.")
            continue
    while True:
        try:
            amount = int(input("Please type the amount to compare: "))
            if amount < 0:
                print("Invalid input. Please type a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please type a positive integer.")
            continue
    res = filtered_by_amount(expenses, operator, amount)
    if not res:
        print("\nThere are no expenses compared to this amount.")
    else:
        display_expenses(res)


def menu(expenses, history):
    print("Command-based console ready.")
    print("Type 'help' to see all commands.\n")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        # Allow inputs starting with ">"
        if user_input.startswith(">"):
            user_input = user_input[1:].strip()

        parts = user_input.split()

        cmd = parts[0].lower()

        # ======================== HELP ============================
        if cmd == "help":
            print("""
Available commands:

  add <apartment> <type> <amount>
  remove apt <apartment>
  remove range <start> <end>
  remove type <type>
  replace <apartment> <type> <amount>

  show
  show apt <apartment>
  show < <amount>

  filter type <type>
  filter < <amount>

  undo
  exit
""")
            continue

        # ======================== EXIT ============================
        if cmd == "exit":
            print("Goodbye!")
            break

        # ======================== UNDO ============================
        if cmd == "undo":
            undo(expenses, history)
            print("Undo successful.")
            display_expenses(expenses)
            continue

        # ======================== ADD =============================
        if cmd == "add":
            if len(parts) != 4:
                print("Usage: add <apartment> <type> <amount>")
                continue

            try:
                apt = int(parts[1])
                t = parts[2]
                amount = int(parts[3])
                add_expense(expenses, history, apt, t, amount)
                print("Added.")
            except Exception as e:
                print("Error:", e)
            continue

        # ======================== REMOVE ==========================
        if cmd == "remove":
            if len(parts) < 3:
                print("Usage: remove apt <n> | remove range <a> <b> | remove type <t>")
                continue

            sub = parts[1]

            if sub == "apt":
                if len(parts) != 3:
                    print("Usage: remove apt <apartment>")
                    continue
                try:
                    apt = int(parts[2])
                    remove_apartment(expenses, history, apt)
                    print("Removed.")
                except Exception as e:
                    print("Error:", e)

            elif sub == "range":
                if len(parts) != 4:
                    print("Usage: remove range <start> <end>")
                    continue
                try:
                    start = int(parts[2])
                    end = int(parts[3])
                    remove_apartments_range(expenses, history, start, end)
                    print("Removed.")
                except Exception as e:
                    print("Error:", e)

            elif sub == "type":
                if len(parts) != 3:
                    print("Usage: remove type <type>")
                    continue
                t = parts[2]
                try:
                    remove_type(expenses, history, t)
                    print("Removed.")
                except Exception as e:
                    print("Error:", e)

            continue

        # ======================== REPLACE =========================
        if cmd == "replace":
            if len(parts) != 4:
                print("Usage: replace <apartment> <type> <amount>")
                continue
            try:
                apt = int(parts[1])
                t = parts[2]
                amount = int(parts[3])
                replace_amount(expenses, history, apt, t, amount)
                print("Replaced.")
            except Exception as e:
                print("Error:", e)
            continue

        # ======================== SHOW ============================
        if cmd == "show":
            # show
            if len(parts) == 1:
                display_expenses(expenses)
                continue

            # show apt X
            if len(parts) == 3 and parts[1] == "apt":
                try:
                    apt = int(parts[2])
                    display_expenses_by_apartment(expenses, apt)
                except ValueError:
                    print("Apartment must be an integer.")
                continue

            # show < amount
            if len(parts) == 3 and parts[1] == "<":
                try:
                    amount = int(parts[2])
                    res = filtered_by_amount(expenses, "<", amount)
                    display_expenses(res)
                except ValueError:
                    print("Amount must be an integer.")
                continue

            print("Invalid show command.")
            continue

        # ======================== FILTER ==========================
        if cmd == "filter":
            if len(parts) < 3:
                print("Usage: filter type <t> | filter < <amount>")
                continue

            sub = parts[1]

            # filter type gas
            if sub == "type" and len(parts) == 3:
                t = parts[2]
                res = filtered_by_type(expenses, t)
                display_expenses(res)
                continue

            # filter < 30
            if sub == "<" and len(parts) == 3:
                try:
                    amount = int(parts[2])
                    res = filtered_by_amount(expenses, "<", amount)
                    display_expenses(res)
                except ValueError:
                    print("Amount must be an integer.")
                continue

            print("Invalid filter command.")
            continue

        # ======================== UNKNOWN =========================
        print("Unknown command. Type 'help'.")
