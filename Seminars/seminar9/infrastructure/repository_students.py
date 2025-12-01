from errors.exceptions import RepositoryError


class RepositoryStudents:
    def __init__(self):
        self.__students ={}

    def add_student(self, student):
        if student.id_student in self.__students:
            raise RepositoryError("Student {} already exists".format(student.id_student))
        self.__students[student.id_student] = student

    def get_all(self):
        return list(self.__students.values())