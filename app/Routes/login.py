import os

from flask import Blueprint, request, jsonify

URL_PREFIX = "/login"

mock_user = {
    "username": "Ricardo",
    "password": "123456",
}

API_KEY = os.getenv("API_KEY", "iHQ^msSp;jmG3!ZWO.1y2%*^SX;JmSniI-wHHjam=33fQzmwkwCg-du*drhVaLtA")

login_blueprint = Blueprint('login_bp', __name__, url_prefix=URL_PREFIX)


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

    print(token)
    print(API_KEY)

    if token != API_KEY:
        return jsonify({'message': 'Invalid token.'}), 401

    data = request.json

    username_req = data.get("username")
    password_req = data.get("password")

    print(username_req)
    print(password_req)

    if username_req != mock_user["username"] or password_req != mock_user["password"]:
        return jsonify({'message': 'Wrong username or password.'}), 401

    token = ""

    return jsonify({'message': 'Welcome', 'token': token}), 200
