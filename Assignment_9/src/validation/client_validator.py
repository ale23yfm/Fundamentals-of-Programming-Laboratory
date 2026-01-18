from configobj.validate import is_integer

from errors.errors import ValidationError


class ClientValidator:
    @staticmethod
    def validate(client):
        error =[]
        if client.client_id < 0 or not(is_integer(client.client_id)):
            error.append("client ID is invalid. It must be a positive integer.")
        if len(client.name.strip()) == 0:
            error.append("Name cannot be empty")

        if error:
            raise ValidationError("\n".join(error))