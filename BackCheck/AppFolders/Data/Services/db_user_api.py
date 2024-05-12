from gotrue.errors import AuthApiError
from AppFolders.Data.Database import Database


class UserService(Database):

    def __init__(self):
        super().__init__()

    def get_user_by_external_id(self, external_id: str):
        try:
            data, count = self.db_connection.table("user_profile").select("*").eq("external_id",
                                                                                  external_id).execute()
            if not data[1]:
                return None

            return data[1][0]

        except AuthApiError as e:
            raise e

    def get_user_by_username(self, username: str):
        try:
            data, count = self.db_connection.table("user_profile").select("*").eq("username",
                                                                                  username).execute()
            if not data[1]:
                return None

            return data[1][0]

        except AuthApiError as e:
            raise e

    def create_user_profile(self, external_id: str, username: str):

        if self.get_user_by_external_id(external_id=external_id) is not None:
            return "User already exists", None

        try:
            data, count = self.db_connection.table("user_profile").insert(
                {'external_id': external_id, 'username': username}).execute()

            return None, data[0]

        except AuthApiError as e:
            raise e
