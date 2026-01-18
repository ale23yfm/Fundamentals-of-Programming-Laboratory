from domain.rental import Rental
from errors.errors import RepositoryError


class InMemoryRepository:
    def __init__(self):
        self.__entities = []

    def add(self, entity):
        self.__entities.append(entity)

    def get_all(self):
        return list(self.__entities)

    def remove(self, entity):
        if entity in self.__entities:
            self.__entities.remove(entity)
        else:
            raise RepositoryError("Entity not found")

    def update(self, entity, new_entity):
        try:
            idx = self.__entities.index(entity)
            self.__entities[idx] = new_entity
        except ValueError:
            raise RepositoryError("Entity not found")

    def find_by_id(self, rental_id):
        for e in self.__entities:
            if isinstance(e, Rental) and e.rental_id == rental_id:
                return e
        return None