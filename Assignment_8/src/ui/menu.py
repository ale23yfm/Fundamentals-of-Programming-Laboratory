class Menu:
    def __init__(self, service):
        self.__service = service

    def menu(self):
        print("Welcome to the menu!")
        while True:
            print("\nChoose one option:")
            print("1. Add a student")
            print("2. Display all students")
            print("3. Display by deleting a specific group")
            print("4. Undo")
            print("5. Exit")

            try:
                o = int(input("Your choice from 1-5:"))
            except ValueError:
                print("You should choose a number between 1-5. Try again.")
                continue

            if o == 1:
                while True:
                    try:
                        student_id = int(input("ID: "))
                        break
                    except ValueError:
                        print("Invalid ID. Try again.")
                while True:
                    try:
                        name = input("Name: ")
                        break
                    except ValueError:
                        print("Invalid name. Try again.")
                while True:
                    try:
                        group = int(input("Group: "))
                        break
                    except ValueError:
                        print("Invalid group. Try again.")
                self.__service.add_student(student_id, name, group)

                print("\nThis is your current list of students:")
                for s in self.__service.get_all():
                    print(s)

            if o == 2:
                for s in self.__service.get_all():
                    print(s)

            if o == 3:
                while True:
                    try:
                        group = int(input("Group to delete: "))
                        break
                    except ValueError:
                        print("Invalid group. Try again.")
                c = self.__service.filter_group(group)
                if c == 0:
                    print("\nNothing to delete.")
                else:
                    print("\nThis is your current list of students:")
                    for s in self.__service.get_all():
                        print(s)

            if o == 4:
                try:
                    self.__service.undo()
                    print("Successfully undo!")
                except Exception as e:
                    print(f"{e}")

                print("\nThis is your current list of students:")
                for s in self.__service.get_all():
                    print(s)

            if o == 5:
                print("Thanks for playing!")
                exit()