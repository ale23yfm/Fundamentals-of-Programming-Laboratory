from src.errors.errors import RepositoryError
from src.repository.in_memory_repo import InMemoryRepository
import os
import pickle


class BinaryFileRepository(InMemoryRepository):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.file_path):
            return
        try:
            with open(self.file_path, "rb") as f:
                while True:
                    try:
                        super().add(pickle.load(f))
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

    def _write_all(self):
        with open(self.file_path, "wb") as f:
            for e in super().get_all():
                pickle.dump(e, f)

    def add(self, entity):
        super().add(entity)
        self._write_all()

    def remove(self, entity):
        super().remove(entity)
        self._write_all()

    def update(self, old_entity, new_entity):
        super().update(old_entity, new_entity)
        self._write_all()