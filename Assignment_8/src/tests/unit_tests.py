import unittest
import os
from ..domain.student import Student
from ..services.services import StudentService
from ..repository.repo import MemoryRepository, TextFileRepository, BinaryFileRepository
from ..domain.student_validation import StudentValidation

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.validator = StudentValidation()
        self.memory_repo = MemoryRepository()
        self.service = StudentService(self.validator, self.memory_repo)

    def test_add_student(self):
        self.service.add_student(1, "Ana", 911)
        students = self.service.get_all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Ana")
        self.assertEqual(students[0].group, 911)

    def test_add_duplicate_id_raises(self):
        self.service.add_student(1, "Ana", 911)
        with self.assertRaises(Exception):
            self.service.add_student(1, "Ion", 912)

    def test_filter_group(self):
        self.service.add_student(1, "Ana", 911)
        self.service.add_student(2, "Ion", 912)
        self.service.add_student(3, "Maria", 911)
        count = self.service.filter_group(911)
        students = self.service.get_all()
        self.assertEqual(count, 2)
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Ion")

    def test_undo(self):
        self.service.add_student(1, "Ana", 911)
        self.service.add_student(2, "Ion", 912)
        self.service.undo()
        students = self.service.get_all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Ana")


class TestFileRepositories(unittest.TestCase):
    def setUp(self):
        self.text_file = "test_students.txt"
        self.binary_file = "test_students.bin"
        if os.path.exists(self.text_file):
            os.remove(self.text_file)
        if os.path.exists(self.binary_file):
            os.remove(self.binary_file)

    def tearDown(self):
        if os.path.exists(self.text_file):
            os.remove(self.text_file)
        if os.path.exists(self.binary_file):
            os.remove(self.binary_file)

    def test_textfile_repo_add_and_load(self):
        repo = TextFileRepository(self.text_file)
        student = Student(1, "Ana", 911)
        repo.add(student)
        repo2 = TextFileRepository(self.text_file)
        students = repo2.get_all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Ana")

    def test_binaryfile_repo_add_and_load(self):
        repo = BinaryFileRepository(self.binary_file)
        student = Student(1, "Ana", 911)
        repo.add(student)
        repo2 = BinaryFileRepository(self.binary_file)
        students = repo2.get_all()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0].name, "Ana")
