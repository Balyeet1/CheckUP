from flask_cors import CORS
from flask import Blueprint
from dotenv import load_dotenv
from BackCheck.app.Routes import blueprints
from BackCheck.app import set_token_key, set_token_timeout
import os

BASE_URL = "/checkup_api"


def setup_app(app):
    """This method receives an app(Flask Object), and configures it."""
    # Load the .env file to be able to interact with it (get the values)
    load_dotenv()

    # Get the current environment, from the .env file and sets it to Pascal Case
    environment = os.getenv("FLASK_ENV").title()

    # So it doesn't have CORS problems
    CORS(app)

    # Gets the configurations from the config.py file, and sets the
    # configs to the app instance(Flask Object), depending of the current environment
    app.config.from_object(f'Configs.config.{environment}Config')

    # To use the token_utilis object, it has to set the token_key and timeout
    set_token_key(app.config["TOKEN_KEY"])
    set_token_timeout(app.config["TOKEN_TIMEOUT"])

    # Using blueprint to build up the URL to interact with this app
    # First created a base blueprint, which will contain the app name_API
    base_bp = Blueprint('base_bp', __name__, url_prefix=BASE_URL)

    # Then nested the users_bp routes into the base_bp, so the URL will concat - Example: /checkup_api/users
    for blueprint in blueprints:
        base_bp.register_blueprint(blueprint)

    # Then add all the prefix to the app itself
    app.register_blueprint(base_bp)
