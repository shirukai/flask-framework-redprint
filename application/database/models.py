# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 17:38
数据库表模型
"""
import uuid
from datetime import datetime
from pytz import timezone

from application import db


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.Integer, nullable=False)
    blogs = db.relationship('Blog', backref='User', lazy='dynamic')

    USER = 0
    ADMIN = 1

    def __init__(self, name, role):
        self.id = str(uuid.uuid1())
        self.name = name
        self.role = role

    def dict(self, select_blog=False):
        user = {
            "id": self.id,
            "name": self.name,
            "role": self.role
        }
        if select_blog:
            user['blogs'] = [blog.dict() for blog in self.blogs]
        return user

    def __repr__(self):
        return 'User %r' % self.name


class Blog(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    context = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    modify_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, context, user_id):
        self.id = str(uuid.uuid1())
        self.title = title
        self.context = context
        self.user_id = user_id
        self.create_time = datetime.now(timezone('Asia/Shanghai')).replace(tzinfo=None)

    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'context': self.context,
            'user': self.User.dict(),
            'create_time': format_time(self.create_time),
            'modify_time': format_time(self.modify_time)
        }


def format_time(time, fmt="%Y-%m-%d %H:%M:%S"):
    if time:
        return time.strftime(fmt)
    else:
        ""
