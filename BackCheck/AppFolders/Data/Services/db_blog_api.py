from gotrue.errors import AuthApiError
from AppFolders.Data.Database import Database


class BlogService(Database):

    def __init__(self):
        super().__init__()

    def get_user_blogs_headers(self, user_id: int):
        try:
            data, count = self.db_connection.table("blog").select("id, title, image, created_at").eq("user_id",
                                                                                                     user_id).order(
                'created_at', desc=True).execute()

            if not data[1]:
                return None

            return data[1]

        except AuthApiError as e:
            raise e

    def create_blog(self, user_id: int, blog_data: dict):

        try:
            data_return, _ = self.db_connection.table("blog_content").insert(
                {"content": blog_data["content"]}).execute()

            if not data_return[1]:
                return None

            blog = data_return[1][0]

            data, count = self.db_connection.table("blog").insert(
                {
                    'user_id': user_id, "title": blog_data["title"], "image": blog_data["image"],
                    "blog_content_id": blog["id"]
                }).execute()

            return data[0]

        except AuthApiError as e:
            print(e.message)
            return None

    def edit_blog(self, user_id: int, blog_data: dict):
        try:
            data_return, _ = self.db_connection.table("blog_content").insert(
                {"content": blog_data["content"]}).execute()

            if not data_return[1]:
                return None

            blog = data_return[1][0]

            data, count = self.db_connection.table("blog").insert(
                {
                    'user_id': user_id, "title": blog_data["title"], "image": blog_data["image"],
                    "blog_content_id": blog["id"]
                }).execute()

            return data[0]

        except AuthApiError as e:
            print(e.message)
            return None
