from AppFolders.Data.Models import User
from AppFolders.Data.Services import UserService, BlogService
from gotrue.errors import AuthApiError
import os


class BlogController:

    def __init__(self, user_service: UserService, blog_service: BlogService):
        self.user_service = user_service
        self.blog_service = blog_service

    def get_user_blog_headers(self, user: User):

        try:
            blogs = self.blog_service.get_user_blogs_headers(user_id=user.get_id())

        except AuthApiError as e:
            return e.message, None

        return None, blogs

    def create_user_blog(self, user: User, blog_data: dict):

        try:
            if blog_data["image"] is not None:
                filename = blog_data["image"].filename
                blog_data["image"].save(os.path.join('AppFolders', 'Images', 'Blog', filename))
                blog_data["image"] = filename

            blog = self.blog_service.create_blog(user_id=user.get_id(), blog_data=blog_data)

            if blog is None:
                return "Failed to create Blog.", None

        except AuthApiError as e:
            return e.message, None

        return None, blog
