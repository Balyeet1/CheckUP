from .database_api import Database

database = Database()


def set_database_connection(url, key):
    """This function receives an url and key, and set in the database object
        already created."""
    database.connect_DB(url, key)


__all__ = [
    "database",
    "set_database_connection",
]
