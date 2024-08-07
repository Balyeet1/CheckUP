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


@blog_blueprint.route('/get', methods=['GET'], endpoint='/get')
@validate_API_and_token_wrapper
def get_blog(user: User):
    blog_id_string = request.args.get("id")

    if not blog_id_string:
        return jsonify({'message': 'Missing Data'}), 400

    try:
        blog_id = int(blog_id_string)
    except ValueError:
        return jsonify({'message': 'Id is not a string'}), 400

    error, blog = blogController.get_blog_by_id(user=user, blog_id=int(blog_id))

    if error is not None:
        return jsonify({'message': error}), 400

    return jsonify({'blog': blog.get_blog_dto()}), 200


@blog_blueprint.route('/create', methods=['POST'], endpoint='/create')
@validate_API_and_token_wrapper
def create_blog(user: User):
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


@blog_blueprint.route('<int:blog_id>/edit', methods=['PUT'], endpoint='/edit')
@validate_API_and_token_wrapper
def edit_blog(user: User, blog_id):
    if not request.form:
        return jsonify({'message': 'Missing Data'}), 400

    blog_data = {key: request.form.get(key) for key in ["title", "content"]}
    blog_data["id"] = blog_id
    blog_data["image"] = request.files.get("image")

    error, edite_blog = blogController.edit_blog(user=user, blog_data=blog_data)

    if error is not None:
        return jsonify({'message': error})

    return jsonify({'message': "Blog Updated", 'blog': edite_blog}), 200


@blog_blueprint.route('/delete/<int:blog_id>', methods=['DELETE'], endpoint='/delete')
@validate_API_and_token_wrapper
def delete_blog(user: User, blog_id):
    if not blog_id:
        return jsonify({'message': 'Missing Data'}), 400

    error, message = blogController.delete_blog(user=user, blog_id=int(blog_id))

    if error is not None:
        return jsonify({'message': error})

    return jsonify({'message': message}), 200


@blog_blueprint.route('/images/<filename>')
def get_blog_images(filename: str):
    image_path = blogController.get_blog_image(image_name=filename)

    if image_path is not None:
        return image_path

    image_not_found_path = os.path.join('AppFolders', 'Images', 'image_not_found.png')
    return send_file(image_not_found_path, as_attachment=False)


@blog_blueprint.route('/download/<filename>')
@validate_API_and_token_wrapper
def download_blog_images(user: User, filename: str):
    image_path = blogController.get_blog_image(image_name=filename, user=user)

    if image_path is not None:
        return send_file(image_path, as_attachment=True)

    image_not_found_path = os.path.join('AppFolders', 'Images', 'image_not_found.png')
    return send_file(image_not_found_path, as_attachment=True)
