class Student:
    def __init__(self,id_student, name, group):
            self.__id_student = id_student
            self.__name = name
            self.__group = group

    @property
    def id_student(self):
        return self.__id_student

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @name.setter
    def name(self, name):
        self.__name = name

    @group.setter
    def group(self, group):
        self.__group = group

    def __str__(self):
        return f"{self.__id_student}. {self.__name} (group {self.__group})"