from flask import Blueprint, jsonify, request
from .CheckRequest import validate_API_and_token_wrapper
from AppFolders.Data.Models import User
from AppFolders.Controlers import imageController

URL_PREFIX = "/image"

image_blueprint = Blueprint('image_bp', __name__, url_prefix=URL_PREFIX)


@image_blueprint.route('/list', methods=['GET'], endpoint='/list')
@validate_API_and_token_wrapper
def get_blog_image_url(user: User):
    images_url_list = imageController.get_images_url_list(user=user)

    return jsonify({'images_list': images_url_list}), 200


@image_blueprint.route('/store', methods=['POST'], endpoint='/store')
@validate_API_and_token_wrapper
def get_blog_image_url(user: User):
    if 'file' not in request.files:
        return jsonify({'message': 'Missing Data'}), 400

    imageController.store_image(user=user, image=request.files["file"])

    return jsonify({'image_url': "image url"}), 200
