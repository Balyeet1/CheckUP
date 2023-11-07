from flask import Blueprint, request, jsonify
from app.token import token_utils

URL_PREFIX = "/users"

# Creates a blueprint for the purpose of all the endpoints have a pre default URL prefix
# Example: /Users/list
# Example: /Users/{id}
user_blueprint = Blueprint('user_bp', __name__, url_prefix=URL_PREFIX)


@user_blueprint.route('/list', methods=['GET'])
def users_list():
    if not ("Authorization" in request.headers):
        return jsonify({'message': 'Missing token.'}), 401

    auth = request.headers.get("Authorization").split(" ")

    if len(auth) != 2:
        return jsonify({'message': 'Missing authentication values.'}), 401

    auth_type, token = auth

    if auth_type != "Bearer":
        return jsonify({'message': 'Invalid type of authorization.'}), 401

    decode = token_utils.check_token(token)

    if decode["has_error"]:
        return jsonify({'message': decode["error"]}), 401

    print(decode["data"].claims)

    return jsonify({'message': "Success"}), 200


@user_blueprint.route('/<int:user_id>', methods=['GET', 'POST'])
def region(user_id):
    print(request.method)

    return jsonify({'message': 'User'}), 200
