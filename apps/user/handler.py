from abc import ABC

import jwt
import time

from apps import logger, cf
from apps.default_handler import DefaultHandler, get_json, auth
from apps.user.model import User
from apps.util.encrypt import md5


class LoginHandler(DefaultHandler, ABC):

    @get_json('id', 'password')
    async def post(self, *args, **kwargs):
        id = self.body.get('id')
        pwd = self.body.get('password')
        user = User()
        await user.connect()
        one = await user.select(id, 'password')
        del user
        if one is None:
            self.set_status(404)
            return
        logger.info(md5(pwd))
        if one[0] != md5(pwd):
            self.set_status(400)
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


class UserExistHandler(DefaultHandler, ABC):
    async def get(self, id, *args, **kwargs):
        user = User()
        await user.connect()
        one = await user.select(id)
        if one is None:
            self.set_status(404)
            return


class UserHandler(DefaultHandler, ABC):

    @auth
    async def get(self, *args, **kwargs):
        id = args[0]
        user = User()
        await user.connect()
        one = await user.select(id, 'nickname', 'email', 'avatar', 'gender', 'city', 'summary')
        del user
        if one is None:
            self.set_status(404)
            return
        self.finish({
            'nickname': one[0],
            'email': one[1],
            'avatar': one[2],
            'gender': one[3],
            'city': one[4],
            'summary': one[5],
        })

    @get_json('password', 'email')
    async def post(self, *args, **kwargs):
        id = args[0]
        pwd = self.body.get('password')
        email = self.body.get('email')
        if email != cf.get('server', 'email'):
            self.set_status(400)
            return
        user = User()
        await user.connect()
        count = await user.insert_user(id, md5(pwd), email)
        del user
        if count <= 0:
            self.set_status(400)
            return
        self.set_status(201)

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        id = args[0]
        user = User()
        await user.connect()
        if 'email' in self.body:
            self.set_status(400)
            self.finish()
            return
        if 'password' in self.body:
            self.body['password'] = md5(self.body['password'])
        count = await user.update(id, self.body)
        if count <= 0:
            self.set_status(400)
            return
