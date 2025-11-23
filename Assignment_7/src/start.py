#
# This module is used to invoke the program's UI and start it. It should not contain a lot of code.
#

from functions import generate_random_expenses
from ui import menu

if __name__ == "__main__":
    expenses= generate_random_expenses()
    history = generate_random_expenses()
    menu(expenses, history)
