from .login import login_blueprint
from .user import user_blueprint

blueprints = [
    user_blueprint,
    login_blueprint,
]

__all__ = [
    "blueprints"
]
