# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
tag endpoints
"""

from flask import request
from flask import jsonify

from application.api.v1.tag import business
from application.libs.redprint import RedPrint

api = RedPrint("tag")


@api.route("", methods=['POST'])
def post_tag():
    data = request.get_json()
    return jsonify(business.create_tag(data['name']))


@api.route("/<tag_id>", methods=['PUT'])
def put_tag(tag_id):
    data = request.get_json()
    return jsonify(business.update_tag(tag_id, data['name']))


@api.route("", methods=['GET'])
def get_tags():
    return jsonify(business.get_tags())


@api.route("/<tag_id>", methods=['GET'])
def get_tag(tag_id):
    return jsonify(business.get_tag_by_id(tag_id).dict())


@api.route("/<tag_id>/blogs", methods=['GET'])
def get_tag_and_blogs(tag_id):
    return jsonify(business.get_tag_by_id(tag_id).dict(select_blog=True))


@api.route("/<tag_id>", methods=['DELETE'])
def delete_tag(tag_id):
    return jsonify(business.delete_tag_by_id(tag_id))
