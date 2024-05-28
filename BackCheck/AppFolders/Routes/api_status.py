from flask import Blueprint, jsonify

URL_PREFIX = "status"

status_blueprint = Blueprint('status', __name__, url_prefix=URL_PREFIX)


@status_blueprint.route('', methods=['GET'])
@status_blueprint.route('/', methods=['GET'])
def api_status():
    return jsonify({'status': 'API is up and running'}), 200
