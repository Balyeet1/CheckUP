from gotrue.errors import AuthApiError
from .Database import Database


class Db_User(Database):

    def __init__(self):
        super().__init__()

    def sign_up_user(self, user_email: str, password: str):
        try:
            return None, self.db_connection.auth.sign_up({
                "email": user_email,
                "password": password,
            })

        except AuthApiError as e:
            return e.message

    def sign_in_user(self, user_email: str, password: str):
        try:
            return None, self.db_connection.auth.sign_in_with_password({
                "email": user_email,
                "password": password,
            })
        except AuthApiError as e:
            return e.message
