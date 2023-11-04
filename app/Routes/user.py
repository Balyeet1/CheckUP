from flask import Blueprint, request, jsonify

URL_PREFIX = "/users"

# Creates a blueprint for the purpose of all the endpoints have a pre default URL prefix
# Example: /Users/list
# Example: /Users/{id}
user_blueprint = Blueprint('user_bp', __name__, url_prefix=URL_PREFIX)


@user_blueprint.route('/list', methods=['GET'])
def users_list():

    return jsonify({'message': 'Users list'}), 200


@user_blueprint.route('/<int:user_id>', methods=['GET', 'POST'])
def region(user_id):
    print(request.method)

    return jsonify({'message': 'User'}), 200

