import os
from repository.in_memory_repo import InMemoryRepository

class TextFileRepository(InMemoryRepository):
    def __init__(self, file_path, entity_class):
        super().__init__()
        self.file_path = file_path
        self.entity_class = entity_class
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    super().add(self.entity_class.from_line(line))

    def _write_all(self):
        with open(self.file_path, "w") as f:
            for e in super().get_all():
                f.write(e.to_line() + "\n")

    def add(self, entity):
        super().add(entity)
        self._write_all()

    def remove(self, entity):
        super().remove(entity)
        self._write_all()

    def update(self, old_entity, new_entity):
        super().update(old_entity, new_entity)
        self._write_all()
