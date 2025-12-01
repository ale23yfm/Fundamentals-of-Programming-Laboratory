from Assignment_8.src.domain.student import Student

class StudentService:
    def __init__(self, student_validator, student_repository):
        self.__student_validator = student_validator
        self.__repository = student_repository
        self.__history = []

    def add_student(self, id_student, name, group):
        student = Student(id_student, name, group)
        self.__student_validator.validate_student(student)
        self.__save_history()
        self.__repository.add_student(student)

    def get_all_students(self):
        return self.__repository.get_all()

    def filter_group(self, group):
        self.__save_history()
        students = self.get_all_students()
        list = []
        for s in students:
            if s.group != group:
                list.append(s)
        self.__repository.replace_data(list)

    def undo(self):
        if not self.__history:
            raise Exception("No more undo steps available")
        prev_state = self.__history.pop()
        self.__repository.replace_data(prev_state)

    def __save_history(self):
        self.__history.append(self.__repository.copy_data())

