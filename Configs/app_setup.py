from flask_cors import CORS
from flask import Blueprint
from dotenv import load_dotenv
from app.Routes import user_blueprint
import os

BASE_URL = "/checkUP_API"


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

    # Using blueprint to build up the URL to interact with this app
    # First created a base blueprint, which will contain the app name_API
    base_bp = Blueprint('base_bp', __name__, url_prefix=BASE_URL)

    # Then nested the users_bp routes into the base_bp, so the URL will concat - Example: /CheckUP/Users
    base_bp.register_blueprint(user_blueprint)

    # Then add all the prefix to the app itself
    app.register_blueprint(base_bp)
