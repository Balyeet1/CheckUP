from .login import login_blueprint
from .user import user_blueprint
from .blog import blog_blueprint

blueprints = [
    user_blueprint,
    login_blueprint,
    blog_blueprint,
]

__all__ = [
    "blueprints"
]
