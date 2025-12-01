from Assignment_8.src.repository.repository_exceptation import RepositoryException

class MemoryRepository:
    def __init__(self):
        """
        Initialize an empty memory repository.
        """
        self._data ={}

    def add(self, student):
        """
        Add a student to the list of students.
        :param student: the student to add

        :raises RepositoryException: if the student already exists
        """
        if student._Student__id_student in self._data:
            raise RepositoryException("ID already exists")
        self._data[student._Student__id_student] = student

    def get_all(self):
        """
        Get all students.
        :return: the list of students
        """
        return list(self._data.values())

    def replace(self, list):
        """
        Replace the students in list.
        :param list: temporary list of students
        """
        self._data = {}
        for s in list:
            self._data[s._Student__id_student] = s

    def copy_student(self):
        """
        Copy student from memory.
        :return: the copy of student
        """
        return self.get_all().copy()