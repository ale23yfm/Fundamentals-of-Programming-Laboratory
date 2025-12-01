class Student:
    def __init__(self,id_student, name, value):
            self.__id_student = id_student
            self.__name = name
            self.__value = value

    @property
    def id_student(self):
        return self.__id_student

    @property
    def name(self):
        return self.__name
    @property
    def value(self):
        return self.__value
    @name.setter
    def name(self, name):
        self.__name = name

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return f"{self.id_student}:{self.__name}-> {self.__value}"