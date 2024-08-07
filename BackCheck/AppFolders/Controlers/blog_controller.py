from AppFolders.Data.Models import User
from AppFolders.Data.Services import UserService, BlogService, BlogImagesService
from gotrue.errors import AuthApiError
from AppFolders.Lib.generate_user_bucket_name import generate_user_bucket_name
from typing import Optional


class BlogController:

    def __init__(self, user_service: UserService, blog_service: BlogService, blog_images_service: BlogImagesService):
        self.user_service = user_service
        self.blog_service = blog_service
        self.blog_images_service = blog_images_service

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
                user_bucket = generate_user_bucket_name(user=user)
                self.blog_images_service.store_image(image=blog_data["image"].read(),
                                                     image_name=blog_data["image"].filename, bucket_name=user_bucket)

                blog_data["image"] = blog_data["image"].filename

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
            error, old_blog, edite_blog = self.blog_service.edit_blog(user_id=user.get_id(),
                                                                      blog_data=blog_data)

            # If the blog was not edited successfully, return an error message
            if error is not None:
                return error, None

                # Save the new image
            if file is not None and old_blog.image != edite_blog["image"]:
                print("Storing new image")
                user_bucket = generate_user_bucket_name(user=user)
                self.blog_images_service.store_image(image=file.read(),
                                                     image_name=edite_blog["image"], bucket_name=user_bucket)

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

        except AuthApiError as e:
            return e.message, None

        return None, "Blog deleted successfully."

    def get_blog_image(self, user: User, image_name: str) -> Optional[str]:
        user_bucket = generate_user_bucket_name(user=user)
        if self.blog_images_service.retrieve_image(image_name=image_name, bucket_name=user_bucket) is None:
            return None

        return f'AppFolders/Images/Blog/{image_name}'
