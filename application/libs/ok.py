# encoding: utf-8
"""
@author : shirukai
@date : 2019-05-27 19:48
正常请求处理
"""
from werkzeug.wrappers import Response
from flask import json


def api_success_handler(res=None):
    if isinstance(res, Response):
        code = res.status_code
        if code == 200:
            content_type = 'application/json'
            if res.content_type == content_type:
                data = json.loads(res.data)
            else:
                data = res.data
                res.headers['Content-Type'] = content_type
            result = dict(
                code=0,
                status='succeed',
                data=data
            )
            res.set_data(json.dumps(result))
    return res
