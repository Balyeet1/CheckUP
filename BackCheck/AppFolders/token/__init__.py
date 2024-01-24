from .token import Token

token_utils = Token()


def set_token_key(key):
    """This function receives a token key, and set in the token_utils object
    already created."""
    token_utils.set_key(key)


def set_token_timeout(seconds: int):
    """This function receives an amount of seconds, and sets in the token_utils object
    already created."""
    token_utils.set_timeout(seconds)


__all__ = [
    "set_token_key",
    "token_utils",
    "set_token_timeout",
]
