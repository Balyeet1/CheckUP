from AppFolders.token import token_utils
from flask import current_app, request, jsonify


# TODO: Add max request per minute when validating

def validate_request_header(header):
    """Receives the request header and validates if it has authorization and the type."""
    if not ("Authorization" in header):
        return (jsonify({'message': 'Missing token.'}), 401), None

    auth = header.get("Authorization").split(" ")

    if len(auth) != 2:
        return (jsonify({'message': 'Missing authentication values.'}), 401), None

    auth_type, token = auth

    if auth_type != "Bearer":
        return (jsonify({'message': 'Invalid type of authorization.'}), 401), None

    return None, token


def validate_API_KEY(func):
    """ Validates the header and if the API_key given, is the correct one."""
    def wrapper(*args, **kwargs):
        error, token = validate_request_header(request.headers)

        if error is not None:
            return error

        if token != current_app.config["LOGIN_API_KEY"]:
            return jsonify({'message': 'Invalid token.'}), 401

        return func(*args, **kwargs)

    return wrapper


def validate_token(func):
    """ Validates the header and if the token given, has the right signature
        and a valid token body.
        \n If the token is valid, returns the token_body."""
    def wrapper(*args, **kwargs):
        error, token = validate_request_header(request.headers)

        if error is not None:
            return error

        decode = token_utils.check_token(token)

        if decode["has_error"]:
            return jsonify({'message': decode["error"]}), 401

        return func(*args, **kwargs, token_body=decode["data"].claims)

    return wrapper
