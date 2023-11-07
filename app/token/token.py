import os
from joserfc import jwt
from joserfc.errors import InvalidClaimError, MissingClaimError, BadSignatureError


class Token:

    def __init__(self):
        self.key = None
        self.default_header = {"alg": "RS256", 'typ': 'JWT'}
        self.iss = os.getenv("ISS", "my.checkup.web")
        self.claims = {"iss": self.iss}

    def set_key(self, key):
        self.key = key

    def has_key(self) -> bool:
        return self.key is not None

    def generate_token(self, body: dict) -> str:
        if not self.has_key():
            raise Exception("Plz set a key, before you use this class.")

        token_body = dict(self.claims, **body)

        return jwt.encode(header=self.default_header, claims=token_body, key=self.key)

    def generate_auth_token(self, username: str) -> str:
        body = {
            "username": username,
        }

        return self.generate_token(body)

    def decode(self, token: str) -> dict:
        if not self.has_key():
            raise Exception("Plz set a key, before you use this class.")

        try:
            return {"has_error": False, "data": jwt.decode(token, self.key)}
        except BadSignatureError:
            return {"has_error": True, "error": "Invalid token."}

    def check_claims(self, claims: dict):
        claims_validations = jwt.JWTClaimsRegistry(
            iss={"essential": True, "value": self.iss},
            username={"essential": True},
        )

        try:
            claims_validations.validate(claims)
        except MissingClaimError:
            return "Missing claim."
        except InvalidClaimError:
            return "Wrong value claim."

    def check_token(self, token: str) -> dict:
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

        if validation:
            unencrypted_token["error"] = validation
            return unencrypted_token

        unencrypted_token["has_error"] = False
        unencrypted_token["data"] = decoded_token["data"]

        return unencrypted_token
