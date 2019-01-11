import time
from abc import ABC
import json
import functools

import jwt
from tornado.web import RequestHandler

from apps import logger, cf
from apps.user.model import User
from apps.util.constant import Constant
from apps.util.encrypt import md5


class DefaultHandler(RequestHandler, ABC):
    body = None

    def set_default_headers(self):
        # allow to cross domain
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with, Content-Type, token')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')

    async def options(self, *args, **kwargs):
        pass

    async def put_one(self, table, *args, **kwargs):
        id = int(args[0])
        await table.connect()
        count = await table.update(id, self.body)
        del table
        if count <= 0:
            self.set_status(404)
            self.finish(Constant.resource_not_exists)
            return
        self.finish(Constant.ok)

    async def delete_one(self, table, *args, **kwargs):
        id = int(args[0])
        await table.connect()
        count = await table.delete(id)
        del table
        if count <= 0:
            self.set_status(404)
            self.finish(Constant.resource_not_exists)
            return
        self.finish(Constant.ok)


def get_json(*fields):
    def decorate(func):
        @functools.wraps(func)
        async def wrapper(self: RequestHandler, *args, **kwargs):
            try:
                body = json.loads(self.request.body.decode("utf8"))
            except Exception as e:
                logger.info(e)
                self.set_status(400)
                self.finish(Constant.params_error)
                return
            self.body = body
            if not isinstance(self.body, dict):
                self.set_status(400)
                self.finish(Constant.params_error)
                return
            for p in fields:
                if self.body.get(p, None) is None:
                    self.set_status(400)
                    self.finish(Constant.params_insufficiency)
                    return
            await func(self, *args, **kwargs)

        return wrapper

    return decorate


class IndexHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        self.finish(Constant.ok)


class AuthHandler(DefaultHandler, ABC):

    @get_json('id', 'password')
    async def post(self, *args, **kwargs):
        """
        @api {post} /auth Get access token
        @apiVersion 0.1.0
        @apiName AuthAccessToken
        @apiGroup Auth
        @apiParam {String} id JSON param, the id of the user.
        @apiParam {String} password JSON param, the login password of the user.
        @apiSuccess (201) {String} token The access token.
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 201 Created
            {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
            }
        @apiError (4xx) {Number} code The error code.
        """
        id = self.body.get('id')
        pwd = self.body.get('password')
        user = User()
        await user.connect()
        one = await user.select(id, 'password')
        del user
        if one is None:
            self.set_status(404)
            self.finish(Constant.user_not_exists)
            return
        logger.info(md5(pwd))
        if one[0] != md5(pwd):
            self.set_status(400)
            self.finish(Constant.pwd_error)
            return
        now = int(time.time())
        exp = int(cf.get('server', 'token_exp'))
        payload = {
            "id": id,
            "iat": now,
            "exp": now + exp
        }
        try:
            token = jwt.encode(payload, cf.get('server', 'secret_key'), algorithm='HS256').decode('utf8')
            self.set_status(201)
            self.finish({'token': token, 'expire': exp})
        except Exception as e:
            logger.error(e)
            self.set_status(500)
            self.finish(Constant.internal_error)


def auth_func(self: RequestHandler, func=None, *args, **kwargs):
    token = self.request.headers.get("token", None)
    if token is None:
        self.set_status(401)
        self.finish(Constant.unauthorized)
        return False
    try:
        playload = jwt.decode(token, cf.get('server', 'secret_key'), algorithms=['HS256'],
                              options={"verify_exp": True})

        if playload:
            self.current_user = playload['id']
            self.current_user = None
        else:
            self.set_status(401)
            self.finish(Constant.unauthorized)
            return False
    except Exception as e:
        logger.error(e)
        self.set_status(401)
        self.finish(Constant.unauthorized)
        return False


def auth(func):
    @functools.wraps(func)
    async def wrapper(self: RequestHandler, *args, **kwargs):
        token = self.request.headers.get("token", None)
        if token is None:
            self.set_status(401)
            self.finish(Constant.unauthorized)
            return
        try:
            playload = jwt.decode(token, cf.get('server', 'secret_key'), algorithms=['HS256'],
                                  options={"verify_exp": True})
        except Exception as e:
            logger.error(e)
            self.set_status(401)
            self.finish(Constant.unauthorized)
            return
        else:
            if playload:
                user = User()
                await user.connect()
                one = await user.select(playload['id'])
                del user
                if one is None:
                    self.set_status(401)
                    self.finish(Constant.unauthorized)
                    return
                self.current_user = playload['id']
                await func(self, *args, **kwargs)
                self.current_user = None
            else:
                self.set_status(401)
                self.finish(Constant.unauthorized)

    return wrapper
