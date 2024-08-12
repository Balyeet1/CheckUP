from flask import Blueprint, jsonify
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
