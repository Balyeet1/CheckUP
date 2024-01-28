from .database import connect_database


class Database:

    def __init__(self):
        self.db_connection = None

    def connect_DB(self, url, key):
        """ Method which receives an url and key, so that other methods can use it to interact with the database.
            If not set, the database cant be use."""
        self.db_connection = connect_database(url, key)

    def sign_up_user(self, user_email, password):
        data = self.db_connection.auth.sign_up({
            "email": user_email,
            "password": password,
        })

        return data

    def sign_in_user(self, user_email, password):
        try:
            data = self.db_connection.auth.sign_in_with_password({
                "email": user_email,
                "password": password,
            })
        except Exception as e:
            print(e.args, e)
            return "Something went wrong"

        return data
