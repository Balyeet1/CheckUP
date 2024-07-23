from flask import Blueprint, request, jsonify
from .CheckRequest import validate_API_KEY_wrapper
from AppFolders.Controlers import userController

URL_PREFIX = "/login"

login_blueprint = Blueprint('login_bp', __name__, url_prefix=URL_PREFIX)


@login_blueprint.route(rule='/', methods=['POST'], endpoint='/')
@login_blueprint.route(rule='', methods=['POST'], endpoint='')
@validate_API_KEY_wrapper
def login():
    if not request.json:
        return jsonify({'message': 'Missing Data'}), 400

    if "data" not in request.json:
        return jsonify({'message': 'Missing Data'}), 401

    data = request.json.get("data")

    claims_to_verify = {
        'iss': {"essential": True, "value": "Check"},
        'external': {"essential": True}
    }

    error, claims = userController.decode_token(data, claims_to_verify)

    if error is not None:
        return jsonify({'message': error}), 401

    error, response_token = userController.generate_user_token(external_id=claims["external"])

    if error is not None:
        return jsonify({'message': error}), 404

    return jsonify({'message': 'Successful login', 'user': response_token}), 200
