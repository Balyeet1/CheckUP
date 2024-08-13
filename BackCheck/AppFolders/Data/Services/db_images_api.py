from AppFolders.Data.Database import Database
from typing import Optional
import base64


class ImagesService(Database):

    def __init__(self):
        super().__init__()

    def bucket_exists(self, bucket_name: str) -> bool:
        try:
            self.db_connection.storage.get_bucket(id=bucket_name)
            return True
        except Exception as e:
            print(e)
            return False

    def create_bucket_if_not_exists(self, bucket_name: str):
        try:
            if not self.bucket_exists(bucket_name=bucket_name):
                self.db_connection.storage.create_bucket(id=bucket_name, options={
                    "public": False,
                    "allowedMimeTypes": ['image/*'],
                    "fileSizeLimit": '2MB',
                })
                print(f"Bucket '{bucket_name}' created successfully.")

        except Exception as e:
            print(f"Bucket '{bucket_name}' got a error creating")
            print(e)

    def store_image(self, image, image_name: str, bucket_name: str):
        try:
            self.create_bucket_if_not_exists(bucket_name=bucket_name)

            self.db_connection.storage.from_(bucket_name).upload(image_name, image)

        except Exception as e:
            print(e)
            return None

    def remove_image(self, image_name: str, bucket_name: str) -> Optional[str]:
        try:
            if not self.bucket_exists(bucket_name=bucket_name):
                print("When trying to remove the image, the bucket does´t exists!")
                return None

            response = self.db_connection.storage.from_().upload(image_name)
            return self.db_connection.storage.from_(bucket_name).get_public_url(image_name)
        except Exception as e:
            print(e)
            return None

    def retrieve_image(self, image_name: str, bucket_name: str) -> Optional[str]:
        try:
            if not self.bucket_exists(bucket_name=bucket_name):
                print("When trying to retrieve the image, the bucket does´t exists!!")
                return None

            res = self.db_connection.storage.from_(bucket_name).download(image_name)
            encoded_string = base64.b64encode(res).decode('utf-8')

            return encoded_string

        except Exception as e:
            print(e)
            return None

    def retrieve_image_url(self, image_name: str, bucket_name: str) -> Optional[str]:
        try:
            if not self.bucket_exists(bucket_name=bucket_name):
                print("When trying to retrieve the image, the bucket does´t exists!!")
                return None

            res = self.db_connection.storage.from_(bucket_name).create_signed_url(image_name, 3000)

            return res["signedURL"]

        except Exception as e:
            print(e)
            return None

    def get_all_images_url(self, bucket_name: str) -> Optional[list]:

        try:
            if not self.bucket_exists(bucket_name=bucket_name):
                print("When trying to retrieve the image, the bucket does´t exists!!")
                return None

            res = self.db_connection.storage.from_(bucket_name).list()

            image_names = [item['name'] for item in res]

            public_urls = [{"name": name.split(".")[0],
                            "url": self.db_connection.storage.from_(bucket_name).create_signed_url(name, 5000)[
                                "signedURL"]} for name in image_names]

            return public_urls

        except Exception as e:
            print(e)
            return None
