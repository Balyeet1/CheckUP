import os

from joserfc.jwk import RSAKey


# The configurations variables, that are used to config flask App
class Config(object):
    """This class contains the default configs"""

    # Flask framework related
    DEBUG = False
    TESTING = False

    # App API related
    SECRET_KEY = ""
    LOGIN_API_KEY = ""

    # JWT Related
    TOKEN_KEY = ""
    TOKEN_TIMEOUT = 50000

    # Database related
    DB_URL = ""
    DB_KEY = ""

    """@property
    def DATABASE_URI(self):
        return f'connection/{self.DB_NAME}'  # Change the connection string """  # Use this if need it


class ProductionConfig(Config):
    # App API related
    SECRET_KEY = os.getenv("SECRET_KEY_PROD")
    LOGIN_API_KEY = os.getenv("LOGIN_API_KEY", "iHQ^msSp;jmG3!ZWO.1y2%*^SX;JmSniI-wHHjam=33fQzmwkwCg-du*drhVaLtA")

    # JWT Related
    TOKEN_KEY = RSAKey.import_key(os.getenv("RSA_KEY"))
    TOKEN_TIMEOUT = 500000

    # Database related
    DB_URL = os.getenv("BD_URL_PROD")
    DB_KEY = os.getenv("BD_KEY_PROD")

    # JWT related
    # KEY_SIZE = 2048
    # PARAMETERS = {"use": "enc", "alg": "RSA-OAEP"}
    # TOKEN_KEY = RSAKey.generate_key(key_size=KEY_SIZE, parameters=PARAMETERS)
    # TODO: Test This Later


class DevelopmentConfig(Config):
    # Flask framework related
    DEBUG = True

    # App API related
    SECRET_KEY = os.getenv("SECRET_KEY_DEV")
    LOGIN_API_KEY = os.getenv("LOGIN_API_KEY", "iHQ^msSp;jmG3!ZWO.1y2%*^SX;JmSniI-wHHjam=33fQzmwkwCg-du*drhVaLtA")

    # JWT Related
    TOKEN_KEY = RSAKey.import_key(os.getenv("RSA_KEY"))
    TOKEN_TIMEOUT = 500000

    # Database related
    DB_URL = os.getenv("BD_URL_DEV")
    DB_KEY = os.getenv("BD_KEY_DEV")


class TestingConfig(Config):
    # Flask framework related
    TESTING = True
    DEBUG = True

    # JWT Related
    TOKEN_KEY = RSAKey.import_key(os.getenv("RSA_KEY"))

    # Database related
    DB_URL = ""
    DB_KEY = ""
