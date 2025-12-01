from Assignment_8.src.domain.student import Student

class StudentService:
    def __init__(self, student_validator, student_repository):
        self.__student_validator = student_validator
        self.__repository = student_repository
        self.__history = []

    def add_student(self, id_student, name, group):
        try:
            student = Student(id_student, name, group)
            self.__student_validator.validate(student)
            self.__save_history()
            self.__repository.add(student)
        except Exception as e:
            print(e)

    def get_all(self):
        return self.__repository.get_all()

    def filter_group(self, group):
        self.__save_history()
        students = self.get_all()
        list = []
        c = 0
        for s in students:
            if s.group != group:
                list.append(s)
            else:
                c += 1
        self.__repository.replace(list)
        return c

    def undo(self):
        if not self.__history:
            raise Exception("No more undo steps available")
        prev_state = self.__history.pop()
        self.__repository.replace(prev_state)

    def __save_history(self):
        self.__history.append(self.__repository.copy_student())

