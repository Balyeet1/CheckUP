from AppFolders.Lib.Token import token_utils
from flask import current_app, request, jsonify
from AppFolders.Data.Services import user_service
from AppFolders.Data.Models import User
from typing import Optional


# TODO: Add max request per minute when validating

def user_exists(uuid: str) -> Optional[User]:
    return user_service.get_user_by_username(username=uuid)


def validate_header_token(header):
    """Receives the request header and validates if it has authorization and the type."""
    if not ("Authorization" in header):
        return (jsonify({'message': 'Missing Token.'}), 401), None

    auth = header.get("Authorization").split(" ")

    if len(auth) != 2:
        return (jsonify({'message': 'Missing authentication values.'}), 401), None

    auth_type, token = auth

    if auth_type != "Bearer":
        return (jsonify({'message': 'Invalid type of authorization.'}), 401), None

    return None, token


def validate_API_KEY(headers):
    if not ("X-API-Key" in headers):
        return jsonify({'message': 'Missing Key.'}), 401

    api_key = headers.get("X-API-Key")

    if api_key != current_app.config["LOGIN_API_KEY"]:
        return jsonify({'message': 'Invalid Key.'}), 401


def validate_API_KEY_wrapper(func):
    """ Validates the header and if the API_key given, is the correct one."""

    def wrapper(*args, **kwargs):
        error = validate_API_KEY(request.headers)

        if error is not None:
            return error

        return func(*args, **kwargs)

    return wrapper


def validate_API_and_token_wrapper(func):
    """ Validates the header and if the API key and Token given, has the right signature
        and a valid Token body.
        \n If the API key and Token is valid, returns the token_body."""

    def wrapper(*args, **kwargs):
        error = validate_API_KEY(request.headers)

        if error is not None:
            return error

        error, token = validate_header_token(request.headers)

        if error is not None:
            return error

        decode = token_utils.check_token(token)

        if decode["has_error"]:
            return jsonify({'message': decode["error"]}), 401

        user = user_exists(decode["data"].claims["uuid"])

        if user is None:
            return jsonify({'message': 'unauthorized'}), 401

        return func(*args, **kwargs, user=user)

    return wrapper
