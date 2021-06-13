from flask import Blueprint

from . import authentication, posts, users, comments, errors

api = Blueprint('api', __name__)