from abc import ABC
import json
import functools

import jwt
from tornado.web import RequestHandler

from apps import logger, cf


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
            self.set_status(400)
            return

    async def delete_one(self, table, *args, **kwargs):
        id = int(args[0])
        await table.connect()
        count = await table.delete(id)
        del table
        if count <= 0:
            self.set_status(400)
            return

    async def delete_all(self, table, *args, **kwargs):
        await table.connect()
        count = await table.delete_all()
        del table
        if count <= 0:
            self.set_status(400)
            return


class IndexHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        self.finish({'msg': 'OK'})


def get_json(*fields):
    def decorate(func):
        @functools.wraps(func)
        async def wrapper(self: RequestHandler, *args, **kwargs):
            try:
                body = json.loads(self.request.body.decode("utf8"))
            except Exception as e:
                logger.error(e)
                self.set_status(400)
                return
            self.body = body
            if not isinstance(self.body, dict):
                self.set_status(400)
                return
            for p in fields:
                if self.body.get(p, None) is None:
                    self.set_status(400)
                    return
            await func(self, *args, **kwargs)
        return wrapper
    return decorate


def auth(func):
    @functools.wraps(func)
    async def wrapper(self: RequestHandler, *args, **kwargs):
        token = self.request.headers.get("token", None)
        if token is None:
            self.set_status(401)
            return
        try:
            playload = jwt.decode(token, cf.get('server', 'secret_key'), algorithms=['HS256'], options={"verify_exp": True})

            if playload:
                await func(self, *args, **kwargs)
            else:
                self.set_status(401)
        except Exception as e:
            logger.error(e)
            self.set_status(401)
            return
    return wrapper