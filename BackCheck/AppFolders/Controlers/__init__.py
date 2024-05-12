from .user_controller import UserController
from .blog_controller import BlogController
from AppFolders.Data.Services import user_service, blog_service

blogController = BlogController(user_service=user_service, blog_service=blog_service)
userController = UserController(user_service=user_service)

__all__ = [
    "blogController",
    "userController"
]
