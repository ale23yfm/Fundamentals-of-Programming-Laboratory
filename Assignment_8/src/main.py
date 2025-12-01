from Assignment_8.src.services.services import StudentService
from Assignment_8.src.ui.menu import Menu
from Assignment_8.src.domain.student_validation import StudentValidation
from Assignment_8.src.domain.student import Student
from Assignment_8.src.repository.binary_file_repo import BinaryFileRepository
from Assignment_8.src.repository.text_file_repo import TextFileRepository
from Assignment_8.src.repository.memory_file_repo import MemoryRepository
from Assignment_8.src.repository.repo import MemoryRepository
from Assignment_8.src.repository.repo import TextFileRepository
from Assignment_8.src.repository.repo import BinaryFileRepository


def generate_initial_students(service):
    students = [
        (1, "Ana", 911),
        (2, "Matei", 911),
        (3, "Ioana", 912),
        (4, "Mihai", 913),
        (5, "Sara", 914),
        (6, "Mara", 914),
        (7, "Silviu", 915),
        (8, "Tina", 915),
        (9, "Emanuel", 915),
        (10, "Olga", 916)
    ]
    for st in students:
        try:
            service.add_student(*st)
        except:
            pass

if __name__ == "__main__":
    validator = StudentValidation()

    # SWITCH REPOSITORY HERE:
    #repo = MemoryRepository()
    repo = TextFileRepository("students.txt")
    #repo = BinaryFileRepository("students.bin")

    service = StudentService(validator, repo)

    # Generate initial students only if repo is empty
    if len(service.get_all()) == 0:
        generate_initial_students(service)
        repo.save_to_file()

    ui = Menu(service)
    ui.menu()