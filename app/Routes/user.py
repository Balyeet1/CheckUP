from flask import Blueprint, request, jsonify
from .CheckRequest import validate_token

URL_PREFIX = "/users"

# Creates a blueprint for the purpose of all the endpoints have a pre default URL prefix
# Example: /Users/list
# Example: /Users/{id}
user_blueprint = Blueprint('user_bp', __name__, url_prefix=URL_PREFIX)


@user_blueprint.route('/list', methods=['GET'], endpoint='/list')
@validate_token
def users_list(token_body):

    print(token_body)

    return jsonify({'message': "Success"}), 200


@user_blueprint.route('/<int:user_id>', methods=['GET', 'POST'], endpoint='/<int:user_id>')
@validate_token
def region(user_id):
    print(user_id)

    return jsonify({'message': 'User'}), 200
