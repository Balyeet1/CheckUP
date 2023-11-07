from .token import Token

token_utils = Token()


def set_token_key(key):
    """This function receives a token key, and set in the token_utils object
    already created."""
    token_utils.set_key(key)


__all__ = [
    "set_token_key",
    "token_utils"
]
