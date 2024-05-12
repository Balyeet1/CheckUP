import os
from AppFolders.Lib.Token import set_token_key, set_token_timeout
from AppFolders.Data.Database import connect_database
from AppFolders.Data.Services import set_database_connection
from AppFolders.Routes import blueprints
from dotenv import load_dotenv
from flask import Blueprint
from flask_cors import CORS

BASE_URL = "/checkup_api"


def setup_app(app):
    """This method receives an AppFolders(Flask Object), and configures it."""
    # Load the .env file to be able to interact with it (get the values)
    load_dotenv()

    # Get the current environment, from the .env file and sets it to Pascal Case
    environment = os.getenv("FLASK_ENV").title()

    # So it doesn't have CORS problems
    CORS(app)

    # Gets the configurations from the config.py file, and sets the
    # configs to the AppFolders instance(Flask Object), depending of the current environment
    app.config.from_object(f'AppFolders.Configs.config.{environment}Config')

    # To use the token_utilis object, it has to set the token_key and timeout
    set_token_key(app.config["TOKEN_KEY"])
    set_token_timeout(app.config["TOKEN_TIMEOUT"])

    # Connects to the Database
    db_connection = connect_database(app.config["DB_URL"], app.config["DB_KEY"])

    # Set connection to all services
    set_database_connection(db_connection)

    # Using blueprint to build up the URL to interact with this AppFolders
    # First created a base blueprint, which will contain the AppFolders name_API
    base_bp = Blueprint('base_bp', __name__, url_prefix=BASE_URL)

    # Then nested the users_bp Routes into the base_bp, so the URL will concat - Example: /checkup_api/users
    for blueprint in blueprints:
        base_bp.register_blueprint(blueprint)

    # Then add all the prefix to the AppFolders itself
    app.register_blueprint(base_bp)
