import os.path

from flask import Blueprint, jsonify, request, send_file
from .CheckRequest import validate_API_and_token_wrapper
from AppFolders.Controlers import blogController
from ..Data.Models import User

URL_PREFIX = "/blog"

blog_blueprint = Blueprint('blog_bp', __name__, url_prefix=URL_PREFIX)


@blog_blueprint.route('/list', methods=['GET'], endpoint='/list')
@validate_API_and_token_wrapper
def blogs_list(user: User):
    error, blogs = blogController.get_user_blog_headers(user=user)

    if error:
        return jsonify({'message': error}), 400

    return jsonify({'blogs': blogs}), 200


@blog_blueprint.route('/create', methods=['POST'], endpoint='/create')
@validate_API_and_token_wrapper
def create_blog(user: User):
    print(user)
    if not request.form:
        return jsonify({'message': 'Missing Data'}), 400

    blog_data = {key: request.form.get(key) for key in ["title", "content"]}
    blog_data["image"] = request.files.get("image")

    if not any(blog_data.values()):
        return jsonify({'message': 'Missing Data'}), 400

    error, blog = blogController.create_user_blog(user=user, blog_data=blog_data)

    if error is not None:
        return jsonify({'message': error})

    return jsonify({'blog': blog}), 201


@blog_blueprint.route('/images/<filename>')
def get_blog_images(filename: str):
    return send_file(os.path.join('AppFolders', 'Images', 'Blog', filename), as_attachment=False)
