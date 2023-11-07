from .token import Token

token_utils = Token()


def set_token_key(key):
    token_utils.set_key(key)


__all__ = [
    "token_utils"
]
