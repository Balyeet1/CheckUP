from AppFolders.token import token_utils
from flask import Blueprint, request, jsonify

from .CheckRequest import validate_API_KEY

URL_PREFIX = "/login"

# Remove this, when connecting to database
mock_user = {
    "username": "Ricardo",
    "password": "123456",
}
# ----------------------------------------

login_blueprint = Blueprint('login_bp', __name__, url_prefix=URL_PREFIX)


@login_blueprint.route(rule='/', methods=['GET'], endpoint='/')
@login_blueprint.route(rule='', methods=['GET'], endpoint='')
@validate_API_KEY
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username != mock_user["username"] or password != mock_user["password"]:
        return jsonify({'message': 'Wrong username or password.'}), 401

    response_token = token_utils.generate_auth_token(username=username)

    return jsonify({'message': 'Successful login', 'token': response_token}), 200
