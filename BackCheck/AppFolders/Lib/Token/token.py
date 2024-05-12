import os
import time

from joserfc import jwt
from joserfc.errors import InvalidClaimError, MissingClaimError, BadSignatureError, ExpiredTokenError


class Token:
    """This class is used to abstract the complexity of working with JWT.
        It's using the joserfc library.
    """

    def __init__(self):
        self.key = None
        self.default_token_header = {"alg": "RSA-OAEP", "enc": "A128GCM"}
        self.iss = os.getenv("ISS", "my.checkup.web")
        self.claims = {"iss": self.iss}
        self.timeout_seconds = 0

    def set_key(self, key):
        """ Method which receives a key, so that other methods can use it to encrypt
            and unencrypte tokens. if not set, some methods from this class won't work."""
        self.key = key

    def set_timeout(self, seconds: int = 1200):
        """ Method which receives a seconds, so it can configure the Token timeout."""
        self.timeout_seconds = seconds

    def has_key(self) -> bool:
        """Checks if the current instance has a key."""
        return self.key is not None

    def generate_token(self, body: dict) -> str:
        """ Method that receives content(body), with the purpose of storing it in the Token.
            \n Can't use it if a key was not set, to set it use "instance_name".set_key(key)."""
        if not self.has_key():
            raise Exception("Plz set a key, before you use this class.")

        # Concatenates the default claim dict, with the body dict.
        token_body = dict(self.claims, **body)

        # Creates the Token with a header, claim(content) and the key.
        return jwt.encode(header=self.default_token_header, claims=token_body, key=self.key)

    def generate_auth_token(self, uuid: str) -> str:
        """ Generates a Token, but specifically for auth, receiving only the necessary
            arguments to create the Token."""
        body = {
            "exp": int(time.time()) + self.timeout_seconds,
            "uuid": uuid,
        }

        return self.generate_token(body)

    def decode(self, token: str) -> dict:
        """ Method that receives a Token, and decodes it.
            \n Return a dict with a property "has_error", if true also comes with "error" property,
            if not, comes with a "Data" property.
            \n Can't use it if a key was not set, to set it use "instance_name".set_key(key)."""
        if not self.has_key():
            raise Exception("Plz set a key, before you use this class.")

        try:
            return {"has_error": False, "data": jwt.decode(token, self.key)}
        except (BadSignatureError, ValueError):
            return {"has_error": True, "error": "Invalid Token."}

    def check_claims(self, claims: dict):
        """ Check if the content(claim) of Token, contains the correct
        values and properties. If it does, return string with the error type."""

        # claims_validations contains what information it's going to be validated
        claims_validations = jwt.JWTClaimsRegistry(
            iss={"essential": True, "value": self.iss},
            uuid={"essential": True},
            exp={"essential": True},
        )

        try:
            claims_validations.validate(claims)
            claims_validations.validate_exp(claims.get("exp"))
        except MissingClaimError:
            return "Missing claim."
        except InvalidClaimError:
            return "Wrong value claim."
        except ExpiredTokenError:
            return "The Token is expired."

    def check_token(self, token: str) -> dict:
        """Receives a Token, decodes it and validates the content(claims).
            \n Return a dict with a property "has_error", if true, the "error" property will come with
            a message, if not, the "Data" property will come with the Token content(claims)."""
        unencrypted_token = {
            "has_error": True,
            "data": "",
            "error": "",
        }

        decoded_token = self.decode(token)

        if decoded_token["has_error"]:
            unencrypted_token["error"] = decoded_token["error"]
            return unencrypted_token

        validation = self.check_claims(decoded_token["data"].claims)

        if validation is not None:
            unencrypted_token["error"] = validation
            return unencrypted_token

        unencrypted_token["has_error"] = False
        unencrypted_token["data"] = decoded_token["data"]

        return unencrypted_token
