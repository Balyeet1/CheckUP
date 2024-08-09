from .user_controller import UserController
from .blog_controller import BlogController
from .image_controller import ImagesController
from AppFolders.Data.Services import user_service, blog_service, images_service

blogController = BlogController(user_service=user_service, blog_service=blog_service,
                                images_service=images_service)
userController = UserController(user_service=user_service)

imageController = ImagesController(images_service=images_service)

__all__ = [
    "blogController",
    "userController",
    "imageController"
]
