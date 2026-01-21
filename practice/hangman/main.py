from pathlib import Path

from practice.hangman.repository.text_file import TextFileRepo
from practice.hangman.service.service import HangmanService


def console(service):
    print("Welcome to HANGMAN! type 'help' to see the available commands")
    while True:
        o = input(">>>>>").lower().strip()
        command, _, argument = o.partition(" ")
        if service.is_in_game():
            if not o:
                continue

            service.guess_letter(o[0])

            print(service.get_masked())
            print(service.get_hangman())

            if service.is_win():
                print("You won!")
                service.restart()
            elif service.is_lost():
                print("You lost!")
                print(f"It was {service._sentence}")
                service.restart()

            continue

        else:
            if command == 'help':
                print ("Available commands:\n"
                       "help\n"
                       "add <sentence>\n"
                       "start\n"
                       "exit\n")
            elif command == 'exit':
                print ("Thanks for trying! Maybe next time you won't be that boring:)")
                return

            elif command == 'start':
                service.start_game()
                print(service.get_masked())
                print(service.get_hangman())
                print("Type your letters now:")

            elif command == 'add':
                try:
                    service.add_sentence(argument)
                except ValueError:
                    print("Invalid sentence. Try again.")
                    continue

            else:
                print("Invalid command, please try again, loser!")
                continue

if __name__=="__main__":
    path = Path(__file__).with_name("hangman.txt")
    repo = TextFileRepo(str(path))
    service = HangmanService(repo)
    console(service)