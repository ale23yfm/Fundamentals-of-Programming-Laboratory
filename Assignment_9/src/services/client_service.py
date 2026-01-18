from domain.client import Client
from errors.errors import ClientError


class ClientService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

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

    def remove_client(self, client_id):
        """
        Function that removes a client
        :param client_id: client's id
        :return: 1 if the client exists, 0 otherwise
        """
        for c in self.__repo.get_all():
            if c.client_id == client_id:
                self.__repo.remove(c)
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
                client = Client(c.client_id, u_name)
                self.__repo.update(c, client)
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