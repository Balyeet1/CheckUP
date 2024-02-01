from .Database.database_con import connect_database
from .db_user_api import Db_User

db_user = Db_User()


def set_database_connection(url, key):
    """This function receives an url and key, and sets in all objects that interact
        with the database."""
    database_connection = connect_database(url, key)

    # Setup of the database in the objects that need to interact with the database
    db_user.connect_DB(database_connection)


__all__ = [
    "db_user",
    "set_database_connection",
]
