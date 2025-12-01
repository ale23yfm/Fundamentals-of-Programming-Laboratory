from domain.student import Student
from errors.exceptions import UIError, ValidationError, RepositoryError


class Console:
    def __init__(self,service_students):
        self.__service_students = service_students
        self.__commands = {
            "add_student":self.__ui_add_student,
            "print_students":self.__ui_print_students
        }

    def __ui_print_students(self,parameters):
        if len(parameters) != 0:
            raise UIError("invalid number of parameters")
        students = self.__service_students.get_all_students()
        if len(students) == 0:
            raise UIError("no students")
        for student in students:
            print(student)

    def __ui_add_student(self,parameters):
        if len(parameters) != 3:
            raise UIError("Invalid number of arguments")
        try:
            id_student = int(parameters[0])
        except ValueError:
            raise UIError("invalid numerical value for student ID")
        name = parameters[1]
        try:
            value = float(parameters[2])
        except ValueError:
            raise UIError("invalid numerical value for student value")
        self.__service_students.add_student(id_student, name, value)
        print("student added successfully")

    def run(self):
        while True:
            command_text = input(">>>").lower().strip()
            if command_text == "":
                continue
            if command_text == "exit":
                print("sayonara,Karen!")
                return
            command_parts = command_text.split(" ")
            command_name = command_parts[0]
            parameters = command_parts[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](parameters)
                except UIError as ui_error:
                    print(f"ui error:{ui_error}")
                except ValidationError as validation_error:
                    print(f"validation error:{validation_error}")
                except RepositoryError as repository_error:
                    print(f"repository error:{repository_error}")
            else:
                print(f"Unknown command:{command_text}")