from AppFolders.Data.Services import UserService
from AppFolders.Lib.Token import token_utils
from gotrue.errors import AuthApiError
import os

# TODO Change this for the token_utils object
from joserfc import jwt
from joserfc.errors import InvalidClaimError, MissingClaimError, BadSignatureError


class UserController:

    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.default_claims = {
            'aud': {"essential": True, "value": "Back Check"},
            'iss': {"essential": True, "value": "Check"},
        }

    def decode_token(self, token: str, claims: dict):
        # TODO Change this method for the token_utils object
        key = os.getenv("TOKEN_32")

        all_claims = {**self.default_claims, **claims}

        claims_validations = jwt.JWTClaimsRegistry(**all_claims)

        try:
            decode_value = jwt.decode(token, key)
        except BadSignatureError:
            print("Error on signature")
            return BadSignatureError.error, None

        try:
            claims_validations.validate(decode_value.claims)
            claims_validations.validate_exp(decode_value.claims.get("exp"))
            return None, decode_value.claims

        except MissingClaimError:
            return "Missing claim.", None
        except InvalidClaimError:
            return "Wrong value claim.", None

    def generate_user_token(self, external_id: str):
        try:
            user = self.user_service.get_user_by_external_id(external_id=external_id)
        except AuthApiError as e:
            return e.message, None

        if user is None:
            return "User does not exists.", None

        response_token = token_utils.generate_auth_token(uuid=user['username'])

        return None, response_token

    def create_user_profile(self, external_id: str, username: str):
        try:
            error, user = self.user_service.create_user_profile(external_id=external_id, username=username)

        except AuthApiError as e:
            print(e.message)
            return False

        return True
