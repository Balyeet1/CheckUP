from flask import Blueprint, jsonify, request
from .CheckRequest import validate_API_KEY_wrapper
from AppFolders.Controlers import userController

URL_PREFIX = "/users"

# Creates a blueprint for the purpose of all the endpoints have a pre default URL prefix
# Example: /Users/list
# Example: /Users/{id}
user_blueprint = Blueprint('user_bp', __name__, url_prefix=URL_PREFIX)


@user_blueprint.route('/create', methods=['GET'], endpoint='/create')
@validate_API_KEY_wrapper
def create_user():
    if not hasattr(request, "data"):
        return jsonify({'message': 'Missing Data'}), 401

    data = request.data.decode()

    claims_to_verify = {
        'iss': {"essential": True, "value": "Create_Profile"},
        'external': {"essential": True},
        'username': {"essential": True},
    }

    error, claims = userController.decode_token(data, claims_to_verify)

    if error is not None:
        return jsonify({'message': error}), 401

    error, user = userController.create_user_profile(external_id=claims["external"], username=claims["username"])

    if error is not None:
        return jsonify({'message': 'Something went wrong'}), 405

    return jsonify({'message': "User created with success"}), 200
