# repo.py
import os
import pickle
import json
from ..domain.student import Student
from ..repository.repository_exceptation import RepositoryException

class BaseRepository:
    """Interface for all repositories"""
    def add(self, student):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def replace_data(self, new_list):
        raise NotImplementedError

    def save_to_file(self):
        pass  # Only needed for file-based repos


class MemoryRepository(BaseRepository):
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



class BinaryFileRepository(MemoryRepository):
    def __init__(self, filename):
        """
        Initialize an empty memory repository.
        """
        super().__init__() #inheritance
        self.__filename = filename
        self._load()

    def _load(self):
        """
        Load the data from the file.
        :return: the data
        """
        if os.path.exists(self.__filename):
            with open(self.__filename, "rb") as f:
                self._data = pickle.load(f)

    def _save(self):
        """
        Save the data to the file.
        :return: the data
        """
        with open(self.__filename, "wb") as f:
            pickle.dump(self._data, f)

    def add(self, student):
        """
        Add a student to the list of students.
        :param student: the student to add
        """
        super().add(student)
        self._save()

    def replace(self, new_list):
        """
        Replace the students in list.
        :param new_list: a temporary list of students
        """
        super().replace(new_list)
        self._save()

    def copy_student(self):
        """
        Copy student from memory.
        :return: the list of students
        """
        return list(self._data.values())



class TextFileRepository(MemoryRepository):
    def __init__(self, filename):
        """
        Initialize an empty memory repository.
        """
        super().__init__() #inheritance
        self.__filename = filename
        self._load_from_file()

    def _load_from_file(self):
        """
        Load the data from the file.
        """
        if not os.path.exists(self.__filename):
            return
        with open(self.__filename, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                id_s, name, group = line.strip().split(",")
                super().add(Student(int(id_s), name, int(group)))

    def save_to_file(self):
        """
        Save the data to the file.
        """
        with open(self.__filename, "w") as f:
            for st in self.get_all():
                f.write(f"{st.id_student},{st.name},{st.group}\n")

    def add(self, student):
        """
        Add a student to the list of students.
        :param student: the student to add
        """
        super().add(student)
        self.save_to_file()

    def replace(self, new_list):
        """
        Replace the students in list.
        :param new_list: a temporary list of students
        """
        super().replace(new_list)
        self.save_to_file()

    def copy_student(self):
        """
        Copy student from memory.
        :return: the list of students
        """
        return list(self._data.values())



class JsonFileRepository(MemoryRepository):
    def __init__(self, filename):
        """
        Initialize an empty memory repository.
        """
        super().__init__() #inheritance
        self.__filename = filename
        self._load_from_file()

    def _load_from_file(self):
        """
        Load the data from the file.
        """
        if not os.path.exists(self.__filename):
            return
        with open(self.__filename, "r") as f:
            try:
                data = json.load(f)
                for st in data:
                    student = Student(st["id_student"], st["name"], st["group"])
                    super().add(student)
            except json.JSONDecodeError:
                pass

    def _save_to_file(self):
        """
        Save the data to the file.
        """
        with open(self.__filename, "w") as f:
            data = []
            for st in self.get_all():
                data.append({
                    "id_student": st.id_student,
                    "name": st.name,
                    "group": st.group
                })
            json.dump(data, f, indent=4)

    def add(self, student):
        """
        Add a student to the list of students.
        :param student: the student to add
        """
        super().add(student)
        self._save_to_file()

    def replace_data(self, new_list):
        """
        Replace the students in list.
        :param new_list: a temporary list of students
        """
        super().replace_data(new_list)
        self._save_to_file()

    def copy_student(self):
        """
        Copy student from memory.
        :return: the list of students
        """
        return list(self._data.values())