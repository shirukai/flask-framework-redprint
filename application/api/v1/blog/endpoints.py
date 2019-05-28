# encoding: utf-8
"""
@author : shirukai
@date : 2019-04-29 15:25
blog endpoints
"""

from flask import request
from flask import jsonify

from application.api.v1.blog import business
from application.libs.redprint import RedPrint

api = RedPrint("blog")


@api.route("", methods=['POST'])
def post_blog():
    data = request.get_json()
    return jsonify(business.create_blog(data['title'], data['context'], data['user_id'], data['tags']))


@api.route("/<blog_id>", methods=['PUT'])
def put_blog(blog_id):
    data = request.get_json()
    return jsonify(business.update_blog(blog_id, data['title'], data['context'],data['tags']))


@api.route("", methods=['GET'])
def get_blogs():
    return jsonify(business.get_blogs())


@api.route("/<blog_id>", methods=['GET'])
def get_blog(blog_id):
    return jsonify(business.get_blog_by_id(blog_id).dict())


@api.route("/<blog_id>", methods=['DELETE'])
def delete_blog(blog_id):
    return jsonify(business.delete_blog_by_id(blog_id))
