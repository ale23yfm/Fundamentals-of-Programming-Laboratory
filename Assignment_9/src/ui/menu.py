from errors.errors import UIError, RentalError, ClientError, BookError


class Menu:
    def __init__(self, book_service, client_service, rental_service):
        self.__rental_service = rental_service
        self.__book_service = book_service
        self.__client_service = client_service

    def menu(self):
        print("Welcome to the menu!")
        while True:
            print("\nChoose one option:")
            print("1. Add clients/books")
            print("2. Remove clients/books")
            print("3. Update clients/books")
            print("4. List clients/books/rented books")
            print("5. Search clients/books")
            print("6. Rent a book")
            print("7. Return a book")
            print("8. Exit")

            try:
                o = int(input("Your choice from 1-8:"))
            except UIError:
                print("You should choose a number between 1-8. Try again.")
                continue

            if o == 1:
                while True:
                    try:
                        choice = int(input("Your choice (1 = client, 2 = book): "))
                        if choice != 1 and choice != 2:
                            print("You should choose 1 or 2. Try again.")
                            continue
                    except UIError:
                        print("You should choose 1 or 2. Try again.")
                        continue

                    #client
                    if choice == 1:
                        while True:
                            id = int(input("Client ID: "))
                            break
                        while True:
                            name = input("Client's name: ")
                            if name.strip() != "":
                                break
                        try:
                            self.__client_service.add_client(id, name)
                            print("Successfully added!")
                            break
                        except UIError as e:
                            print(f"Error: {e}")
                        except ClientError as e:
                            print(f"Error: {e}")

                    #book
                    if choice == 2:
                        while True:
                            id = int(input("Book ID: "))
                            break
                        while True:
                            title = input("Book's title: ")
                            if title.strip() != "":
                                break
                        while True:
                            author = input("Book's name: ")
                            if author.strip() != "":
                                break
                        try:
                            self.__book_service.add_book(id, title, author)
                            print("Successfully added!")
                        except UIError as e:
                            print(f"Error: {e}")
                        except BookError as e:
                            print(f"Error: {e}")
                    break

            if o == 2:
                while True:
                    try:
                        choice = int(input("Your choice (1 = client, 2 = book): "))
                        if choice != 1 and choice != 2:
                            print("You should choose 1 or 2. Try again.")
                            continue
                    except UIError:
                        print("You should choose 1 or 2. Try again.")
                        continue

                    # client
                    if choice == 1:
                        while True:
                            try:
                                client_id = int(input("Client ID: "))
                                cnt = self.__client_service.remove_client(client_id)

                                if cnt == 0:
                                    print("No such client!")
                                else:
                                    print("Successfully deleted!")
                                break

                            except UIError:
                                print("ID must be an integer!")
                                continue

                    # book
                    if choice == 2:
                        while True:
                            try:
                                book_id = int(input("Book ID: "))
                                cnt = self.__book_service.remove_book(book_id)

                                if cnt == 0:
                                    print("No such book!")
                                else:
                                    print("Successfully deleted!")
                                break

                            except UIError:
                                print("ID must be an integer!")
                                continue
                    break

            if o == 3:
                while True:
                    try:
                        choice = int(input("Your choice (1 = client, 2 = book): "))
                        if choice != 1 and choice != 2:
                            print("You should choose 1 or 2. Try again.")
                            continue
                    except UIError:
                        print("You should choose 1 or 2. Try again.")
                        continue

                    #client
                    if choice == 1:
                        while True:
                            try:
                                client_id = int(input("Client ID: "))
                                name = input("Client's name: ")
                                cnt = self.__client_service.update_client(client_id, name)

                                if cnt == 0:
                                    print("No such client!")
                                else:
                                    print("Successfully updated!")
                                break
                            except UIError:
                                print("ID must be an integer!")

                    #book
                    if choice == 2:
                        while True:
                            try:
                                book_id = int(input("Book ID: "))
                                title = input("Title: ")
                                author = input("Author: ")
                                cnt = self.__book_service.update_book(book_id, title, author)

                                if cnt == 0:
                                    print("No such book!")
                                else:
                                    print("Successfully updated!")
                                break
                            except UIError:
                                print("ID must be an integer!")
                    break

            if o == 4:
                while True:
                    try:
                        choice = int(input("Your choice (1 = client, 2 = book, 3 = rented books): "))
                        if choice != 1 and choice != 2 and choice != 3:
                            print("You should choose 1, 2 or 3. Try again.")
                            continue
                    except UIError:
                        print("You should choose 1, 2 or 3. Try again.")
                        continue

                    #client
                    if choice == 1:
                        print("The list of clients:")
                        for c in self.__client_service.get_all():
                            print(c)

                    #book
                    if choice == 2:
                        print("The list of books:")
                        for b in self.__book_service.get_all():
                            print(b)

                    # rentals
                    if choice == 3:
                        print("The list of rented books:")
                        for r in self.__rental_service.get_all():
                            print(r)
                    break

            if o == 5:
                while True:
                    try:
                        choice = int(input("Your choice (1 = client, 2 = book): "))
                        if choice != 1 and choice != 2:
                            print("You should choose 1 or 2. Try again.")
                            continue
                    except UIError:
                        print("You should choose 1 or 2. Try again.")
                        continue

                    # client search
                    if choice == 1:
                        search_field = input("Search by client ID or name? (ID/Name): ").strip().lower()
                        search_value = input(f"Enter the value to search for in {search_field}: ").strip().lower()

                        print("Search results for clients:")
                        found = False
                        clients = self.__client_service.search_clients(search_field, search_value)
                        if clients:
                            for c in clients:
                                print(c)
                            found = True
                        if not found:
                            print("No matching clients found.")
                        break

                    # book search
                    if choice == 2:
                        search_field = input("Search by book ID, title, or author? (ID/Title/Author): ").strip().lower()
                        search_value = input(f"Enter the value to search for in {search_field}: ").strip().lower()

                        print("Search results for books:")
                        found = False
                        books = self.__book_service.search_books(search_field, search_value)
                        if books:
                            for b in books:
                                print(b)
                            found = True
                        if not found:
                            print("No matching books found.")
                        break

            if o == 6:
                while True:
                    try:
                        book_id = int(input("Book ID: "))
                        client_id = int(input("Client ID: "))
                        rental_id = self.__rental_service.rent_book(book_id, client_id)
                        print(f"Book rented successfully with Rental ID: {rental_id}")
                        print("The list of rented books:")
                        for b in self.__rental_service.get_all():
                            print(b)
                        break
                    except ValueError:
                        print("Please enter a valid number for Book ID and Client ID.")
                    except UIError as e:
                        print(f"Error: {e}")
                    except RentalError as e:
                        print(f"Error: {e}")

            if o == 7:
                while True:
                    try:
                        rental_id = int(input("Rental ID: "))
                        return_id = self.__rental_service.return_book(rental_id)
                        print(f"Book returned successfully")
                        print("The list of rented books:")
                        for b in self.__rental_service.get_all():
                            print(b)
                        break
                    except ValueError:
                        print("Please enter a valid number for Rental ID.")
                    except UIError as e:
                        print(f"Error: {e}")
                    except RentalError as e:
                        print(f"Error: {e}")

            if o == 8:
                print("Thanks for playing!")
                exit()