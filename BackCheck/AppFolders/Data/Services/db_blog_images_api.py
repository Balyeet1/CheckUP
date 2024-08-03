from AppFolders.Data.Database import Database
from typing import Optional


class BlogImagesService(Database):

    def __init__(self):
        super().__init__()
        self.bucket_name = "blog_images"

    def store_image(self, image, image_name: str) -> Optional[str]:
        try:
            response = self.db_connection.storage.from_(self.bucket_name).upload(image_name, image)
            return self.db_connection.storage.from_(self.bucket_name).get_public_url(image_name)

        except Exception as e:
            print(e)
            return None

    def remove_image(self, image_name: str) -> Optional[str]:
        try:
            response = self.db_connection.storage.from_(self.bucket_name).upload(image_name)
            return self.db_connection.storage.from_(self.bucket_name).get_public_url(image_name)
        except Exception as e:
            print(e)
            return None

    def retrieve_image(self, image_name) -> Optional[str]:
        try:
            image_url = self.db_connection.storage.from_(self.bucket_name).sign(image_name, 2000)
            return image_url

        except Exception as e:
            print(e)
            return None
