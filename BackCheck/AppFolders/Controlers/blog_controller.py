from AppFolders.Data.Models import User
from AppFolders.Data.Services import UserService, BlogService
from gotrue.errors import AuthApiError
import os
import time


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

    def get_blog_by_id(self, user: User, blog_id: int):

        try:
            blog = self.blog_service.get_blog_by_id(blog_id=blog_id)

            if not blog or blog.get_user_id() != user.get_id():
                return "Blog does not belong to the user.", None

        except AuthApiError as e:
            return e.message, None

        return None, blog

    def create_user_blog(self, user: User, blog_data: dict):
        try:
            if blog_data["image"] is not None:
                original_filename = blog_data["image"].filename
                filename, file_extension = os.path.splitext(original_filename)
                timestamp = str(time.time()).replace('.', '')
                unique_filename = f"{filename}_{timestamp}{file_extension}"
                blog_data["image"].save(os.path.join('AppFolders', 'Images', 'Blog', unique_filename))
                blog_data["image"] = unique_filename

            blog = self.blog_service.create_blog(user_id=user.get_id(), blog_data=blog_data)

            if blog is None:
                return "Failed to create Blog.", None

        except AuthApiError as e:
            return e.message, None

        return None, blog

    def edit_blog(self, user: User, blog_data: dict):
        try:

            file = blog_data["image"]
            blog_data["image"] = None if file is None else file.filename

            # Call the edit_blog method of the BlogService class
            error, blog_before_edited, edite_blog = self.blog_service.edit_blog(user_id=user.get_id(), blog_data=blog_data)

            # If the blog was not edited successfully, return an error message
            if error is not None:
                return error, None

            if blog_data["image"] != blog_before_edited.get_image():
                if blog_before_edited.get_image() is not None:
                    old_image_path = os.path.join('AppFolders', 'Images', 'Blog', blog_before_edited.get_image())
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                # Save the new image
                if file is not None:
                    file.save(os.path.join('AppFolders', 'Images', 'Blog', blog_data["image"]))

        except AuthApiError as e:
            return e.message, None

        return None, edite_blog

    def delete_blog(self, user: User, blog_id: int):
        try:
            # Call the delete_blog method of the BlogService class
            error, blog_deleted = self.blog_service.delete_blog(user_id=user.get_id(), blog_id=blog_id)

            # If the blog was not deleted successfully, return an error message
            if error is not None:
                return error, None

            if blog_deleted.get_image() is not None:
                image_path = os.path.join("AppFolders", "Images", "Blog", blog_deleted.get_image())
                if os.path.exists(image_path):
                    os.remove(image_path)

        except AuthApiError as e:
            return e.message, None

        return None, "Blog deleted successfully."
