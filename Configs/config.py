import os


# The configurations variables, that are used to config flask App
class Config(object):
    DEBUG = False
    TESTING = False
    DB_NAME = ''
    SECRET_KEY = "Dev"

    @property
    def DATABASE_URI(self):
        return f'connection/{self.DB_NAME}'  # Change the connection string


class ProductionConfig(Config):
    # DB_NAME =
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = os.getenv("BD_NAME_DEV")
    SECRET_KEY = os.getenv("SECRET_KEY_DEV")


class TestingConfig(Config):
    # TESTING = True
    # DEBUG = True
    # DB_NAME =
    pass
