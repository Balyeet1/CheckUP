import os
from flask import Blueprint, request, jsonify
from app.token import token_utils

URL_PREFIX = "/login"

mock_user = {
    "username": "Ricardo",
    "password": "123456",
}

API_KEY = os.getenv("API_KEY", "iHQ^msSp;jmG3!ZWO.1y2%*^SX;JmSniI-wHHjam=33fQzmwkwCg-du*drhVaLtA")

login_blueprint = Blueprint('login_bp', __name__, url_prefix=URL_PREFIX)


# Add max request per minute
# Remover a logica do token para um ficheiro a aprte caso seja preciso ser utilizado em outro lugares no futuro.
@login_blueprint.route(rule='/', methods=['GET'])
@login_blueprint.route(rule='', methods=['GET'])
def login():
    if not ("Authorization" in request.headers):
        return jsonify({'message': 'Missing token.'}), 401

    auth = request.headers.get("Authorization").split(" ")

    if len(auth) != 2:
        return jsonify({'message': 'Missing authentication values.'}), 401

    auth_type, token = auth

    if auth_type != "Bearer":
        return jsonify({'message': 'Invalid type of authorization.'}), 401

    if token != API_KEY:
        return jsonify({'message': 'Invalid token.'}), 401

    username = request.json.get("username")
    password = request.json.get("password")

    if username != mock_user["username"] or password != mock_user["password"]:
        return jsonify({'message': 'Wrong username or password.'}), 401

    response_token = token_utils.generate_auth_token(username=username)

    return jsonify({'message': 'Successful login', 'token': response_token}), 200
