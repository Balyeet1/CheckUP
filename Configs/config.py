import os
from joserfc.jwk import RSAKey


# The configurations variables, that are used to config flask App
class Config(object):
    DEBUG = False
    TESTING = False
    DB_NAME = ""
    SECRET_KEY = ""

    LOGIN_API_KEY = ""

    # JWT Related
    TOKEN_KEY = ""

    @property
    def DATABASE_URI(self):
        return f'connection/{self.DB_NAME}'  # Change the connection string


class ProductionConfig(Config):
    # LOGIN_API_KEY = ""

    # JWT Related
    KEY_SIZE = 2048
    PARAMETERS = {"use": "sig", "alg": "RS256"}
    TOKEN_KEY = RSAKey.generate_key(key_size=KEY_SIZE, parameters=PARAMETERS)

    # DB_NAME =
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = os.getenv("BD_NAME_DEV")
    SECRET_KEY = os.getenv("SECRET_KEY_DEV")
    LOGIN_API_KEY = os.getenv("LOGIN_API_KEY", "iHQ^msSp;jmG3!ZWO.1y2%*^SX;JmSniI-wHHjam=33fQzmwkwCg-du*drhVaLtA")

    # JWT Related
    TOKEN_KEY = RSAKey.import_key(os.getenv("RSA_KEY"))


class TestingConfig(Config):
    # TESTING = True
    DEBUG = True
    # DB_NAME =

    TOKEN_KEY = RSAKey.import_key(os.getenv("RSA_KEY"))
    pass
