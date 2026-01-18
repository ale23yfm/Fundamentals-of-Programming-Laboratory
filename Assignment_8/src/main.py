import os
from .services.services import StudentService
from .ui.menu import Menu
from .domain.student_validation import StudentValidation
from .domain.student import Student
from .repository.repo import MemoryRepository, JsonFileRepository, TextFileRepository, BinaryFileRepository

def read_settings(file_path="settings.properties"):
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    settings = {}
    with open(full_path, "r") as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            key, value = line.split("=")
            settings[key.strip()] = value.strip()
    return settings

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
    settings = read_settings("settings.properties")
    repo_type = settings.get("repository", "memory")
    filename = settings.get("filename", "students.txt")

    validator = StudentValidation()

    if repo_type == "memory":
        repo = MemoryRepository()
    elif repo_type == "text":
        filename = settings.get("filename_text", "students.txt")
        repo = TextFileRepository(filename)
    elif repo_type == "binary":
        filename = settings.get("filename_binary", "students.bin")
        repo = BinaryFileRepository(filename)
    elif repo_type == "json":
        filename = settings.get("filename_json", "students.json")
        repo = JsonFileRepository(filename)
    else:
        raise Exception(f"Unknown repository type: {repo_type}")

    service = StudentService(validator, repo)

    # Generate initial students only if repo is empty
    if len(service.get_all()) == 0:
        generate_initial_students(service)
        repo.save_to_file()

    ui = Menu(service)
    ui.menu()