from domain.student import Student


class ServiceStudents:

    def __init__(self,student_validator,student_repository):
        self.__student_validator = student_validator
        self.__student_repository = student_repository

    def add_student(self, id_student, name, value):
        student = Student(id_student, name, value)
        self.__student_validator.validate_student(student)
        self.__student_repository.add_student(student)

    def get_all_students(self):
        return self.__student_repository.get_all()