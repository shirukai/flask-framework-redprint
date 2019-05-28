# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 19:34
数据访问层
"""
from datetime import datetime

from pytz import timezone

from application import APIException, db
from application.database.models import Blog


def get_blog_by_id(id, ):
    blog = Blog.query.filter(Blog.id == id).one_or_none()
    if blog:
        return blog
    else:
        raise APIException(msg="Blog's id does not exist.")


def get_blogs():
    return [blog.dict() for blog in Blog.query.all()]


def create_blog(title, context, user_id):
    blog = Blog(title=title, context=context, user_id=user_id)
    db.session.add(blog)
    db.session.commit()
    return blog.dict()


def delete_blog_by_id(id):
    blog = get_blog_by_id(id)
    db.session.delete(blog)
    db.session.commit()
    return "successfully deleted."


def update_user(id, title, context):
    blog = get_blog_by_id(id)
    blog.title = title
    blog.context = context
    blog.modify_time = datetime.now(timezone('Asia/Shanghai')).replace(tzinfo=None)
    db.session.add(blog)
    db.session.commit()
    return blog.dict()
