from src.domain.client import Client
from src.domain.rental import Rental
from src.errors.errors import ClientError
from src.services.undo import FunctionCall, Operation, CascadedOperation


class ClientService:
    def __init__(self, repo, validator, undo_service, rental_service=False):
        self.__repo = repo
        self.__validator = validator
        self.__undo_service = undo_service
        self.__rental_service = rental_service

    def get_all(self):
        """
        Function that displays all clients
        :return: the clients
        """
        return self.__repo.get_all()

    def add_client(self, client_id, name):
        """
        Function that adds a client
        :param client_id: client's id
        :param name: client's name
        """
        client = Client(client_id, name)
        self.__validator.validate(client)

        # verify if there are any duplicates
        if any(c.client_id == client_id for c in self.__repo.get_all()):
            raise ClientError(f'Client with id: {client_id} already exists')

        self.__repo.add(client)

        if self.__undo_service:
            undo = FunctionCall(self.__repo.remove, client)
            redo = FunctionCall(self.__repo.add, client)
            op = Operation(undo, redo)
            self.__undo_service.record(op)

    def remove_client(self, client_id):
        """
        Function that removes a client
        :param client_id: client's id
        :return: 1 if the client exists, 0 otherwise
        """
        for c in self.__repo.get_all():
            if c.client_id == client_id:
                old_client = Client(c.client_id, c.name)
                affected_rentals = []
                for r in self.__rental_service.get_all():
                    if r.client_id == client_id and r.is_rented == True:
                        old_rental = Rental(r.rental_id, r.book_id, r.client_id, r.is_rented, r.days)
                        r.is_rented = False
                        affected_rentals.append((r, old_rental))

                self.__repo.remove(c)
                if self.__undo_service:
                    cascaded = CascadedOperation()
                    undo_client = FunctionCall(self.add_client, old_client.client_id, old_client.name)
                    redo_client = FunctionCall(self.remove_client, old_client.client_id)
                    cascaded.add(Operation(undo_client, redo_client))

                    for r, old_rental in affected_rentals:
                        undo_rental = FunctionCall(self.__rental_service._set_rented, r.rental_id, True)
                        redo_rental = FunctionCall(self.__rental_service._set_rented, r.rental_id, False)
                        cascaded.add(Operation(undo_rental, redo_rental))

                    self.__undo_service.record(cascaded)

                return 1
        return 0

    def update_client(self, client_id, u_name):
        """
        Function that updates a client
        :param client_id: client's id
        :param u_name: the name client
        :return: 1 if the client exists, 0 otherwise
        """
        for c in self.__repo.get_all():
            if c.client_id == client_id:
                new_client = Client(c.client_id, u_name)
                old_client = Client(c.client_id, c.name)
                self.__repo.update(c, new_client)

                if self.__undo_service:
                    undo = FunctionCall(self.__repo.update, new_client, old_client)
                    redo = FunctionCall(self.__repo.update, old_client, new_client)
                    op = Operation(undo, redo)
                    self.__undo_service.record(op)
                return 1
        return 0

    def search_clients(self, search_field, search_value):
        """
        Function that searches for clients by id or name
        :param search_field: id or name
        :param search_value: the value to search for
        :return: the found client
        """
        results = []
        search_value = search_value.lower()

        for client in self.__repo.get_all():
            if search_field == "id" and search_value in str(client.client_id).lower():
                results.append(client)
            elif search_field == "name" and search_value in client.name.lower():
                results.append(client)

        return results