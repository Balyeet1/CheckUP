from .user import user_blueprint
from .login import login_blueprint

blueprints = [
    user_blueprint,
    login_blueprint,
]

__all__ = [
    "blueprints"
]
