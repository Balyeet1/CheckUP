from typing import Optional

from gotrue.errors import AuthApiError
from postgrest import APIError

from AppFolders.Data.Database import Database
from AppFolders.Data.Models import Blog


class BlogService(Database):

    def __init__(self):
        super().__init__()

    def get_blog_by_id(self, blog_id: int):

        try:
            # Retrieve the blog with the given ID
            response = (self.db_connection.table("blog").select("title, image, user_id, blog_content(*)")
                        .eq('id', blog_id)
                        .single()
                        .execute())

            if response.data:
                return Blog(**response.data, id=blog_id, content=response.data["blog_content"]["content"],
                            blog_content_id=response.data["blog_content"]["id"])

            return None

        except APIError as e:
            print(e.message)
            return None

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

            return data[1]

        except AuthApiError as e:
            print(e.message)
            return None

    def edit_blog(self, user_id: int, blog_data: dict) -> {Optional[str], Blog}:
        try:
            # Retrieve the blog with the given ID
            old_blog = self.get_blog_by_id(blog_data["id"])

            # Check if the blog belongs to the user
            if not old_blog or old_blog.get_user_id() != user_id:
                return "Blog does not belong to the user.", None

            # Update the blog content
            (self.db_connection.table("blog_content").update({"content": blog_data["content"]})
             .eq("id", old_blog.get_content_id())
             .execute())

            # Update the blog
            data, count = (self.db_connection.table("blog").update({
                "title": blog_data["title"], "image": blog_data["image"],
            }).eq('id', blog_data["id"])
             .eq('user_id', user_id).execute())

            edite_blog = data[1][0]

            return None, old_blog, edite_blog

        except AuthApiError as e:
            print(e.message)
            return "Something went wrong", None

    def delete_blog(self, user_id: int, blog_id: int):
        try:
            # Retrieve the blog with the given ID
            blog = self.get_blog_by_id(blog_id)

            # Check if the blog belongs to the user
            if not blog or blog.get_user_id() != user_id:
                return "Blog does not belong to the user."

            # Deleting the blog content will also delete the record blog associated to the blog_content
            self.db_connection.table("blog_content").delete().eq('id', blog.get_content_id()).execute()

            return None, blog

        except AuthApiError as e:
            print(e.message)
            return "Something went wrong"
