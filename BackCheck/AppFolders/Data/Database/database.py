from supabase._sync.client import SyncClient


class Database:

    def __init__(self):
        self.db_connection = None

    def connect_DB(self, database_con: SyncClient):
        """ Method which receives an url and key, so that other methods can use it to interact with the Database.
            If not set, the Database cant be use."""
        self.db_connection = database_con
