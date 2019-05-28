# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:23

"""
from flask import Blueprint
from application.api.v1.user import endpoints as user_endpoints
from application.api.v1.blog import endpoints as blog_endpoints
from application.api.v1.tag import endpoints as tag_endpoints
from application.api.v1 import socketio


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__, url_prefix="/api/v1")
    user_endpoints.api.register(bp_v1)
    blog_endpoints.api.register(bp_v1)
    tag_endpoints.api.register(bp_v1)
    return bp_v1
