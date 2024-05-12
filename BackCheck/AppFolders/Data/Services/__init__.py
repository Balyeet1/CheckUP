from .db_user_api import UserService
from .db_blog_api import BlogService
from supabase._sync.client import SyncClient

user_service = UserService()
blog_service = BlogService()


def set_database_connection(db_connection: SyncClient):
    """This function receives a db connection, and sets in all objects(services) that interact
        with the database."""

    # Setup of the database in the objects that need to interact with the database
    user_service.connect_DB(db_connection)
    blog_service.connect_DB(db_connection)


__all__ = [
    "user_service",
    "blog_service",
    "UserService",
    "BlogService",
    "set_database_connection",
]
