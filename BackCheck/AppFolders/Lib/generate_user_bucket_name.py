from AppFolders.Data.Models import User
import hashlib


def generate_user_bucket_name(user: User) -> str:
    id_to_encrypt = user.id if user.id is not None else 0
    hashed_id = hashlib.sha256(str(id_to_encrypt).encode()).hexdigest()

    return hashed_id + "_images"
