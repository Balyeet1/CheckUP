from AppFolders.Data.Services import ImagesService
from AppFolders.Data.Models import User
from AppFolders.Lib.generate_user_bucket_name import generate_user_bucket_name
from typing import Optional


class ImagesController:

    def __init__(self, images_service: ImagesService):
        self.images_service = images_service

    def get_images_url_list(self, user: User):
        user_bucket = generate_user_bucket_name(user=user)

        self.images_service.get_all_images_url(user_bucket)

        return None
