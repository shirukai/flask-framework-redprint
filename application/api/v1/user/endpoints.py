# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
user endpoints
"""

from flask import request
from flask import jsonify

from application.api.v1.user import business
from application.libs.redprint import RedPrint

api = RedPrint("user")


@api.route("", methods=['POST'])
def post_user():
    data = request.get_json()
    return jsonify(business.create_user(data['name'], data['role']))


@api.route("/<user_id>", methods=['PUT'])
def put_user(user_id):
    data = request.get_json()
    return jsonify(business.update_user(user_id, data['name'], data['role']))


@api.route("", methods=['GET'])
def get_users():
    return jsonify(business.get_users().dict())


@api.route("/<user_id>", methods=['GET'])
def get_user(user_id):
    return jsonify(business.get_user_by_id(user_id))


@api.route("/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    return jsonify(business.delete_user_by_id(user_id))


@api.route("/<user_id>/blogs")
def get_user_posts(user_id):
    return jsonify(business.get_user_by_id(user_id, select_blogs=True))
