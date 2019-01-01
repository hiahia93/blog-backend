from abc import ABC

import jwt
import time

from apps import logger, cf
from apps.default_handler import DefaultHandler, get_json, auth
from apps.user.model import User
from apps.util.encrypt import md5
from apps.util.constant import Constant


class LoginHandler(DefaultHandler, ABC):

    @get_json('password')
    async def post(self, *args, **kwargs):
        """
        @api {post} /user/:id/login Login
        @apiVersion 0.1.0
        @apiName UserLogin
        @apiGroup User
        @apiParam {String} password The login password of the user.
        @apiSuccess (201) {String} token The access token.
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 201 Created
            {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
            }
        @apiError (4xx) {Number} code The error code.
        """
        id = args[0]
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


class UserExistHandler(DefaultHandler, ABC):
    async def get(self, id, *args, **kwargs):
        """
        @api {post} /user/:id/exists Check whether user exists
        @apiVersion 0.1.0
        @apiName UserExists
        @apiGroup User
        @apiSuccess (200) {Number} code success code.
        @apiError (404) {Number} code The error code.
        """
        user = User()
        await user.connect()
        one = await user.select(id)
        if one is None:
            self.set_status(404)
            self.finish(Constant.user_not_exists)
            return
        self.finish(Constant.ok)


class UserHandler(DefaultHandler, ABC):

    @auth
    async def get(self, *args, **kwargs):
        """
        @api {get} /user/:id Get user information
        @apiVersion 0.1.0
        @apiName UserInfo
        @apiGroup User
        @apiPermission Authentication
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (200) {String} token The access token.
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "nickname": "Edgar",
                "email": "doforce@126.com",
                "avatar": null,
                "gender": 0,
                "city": null,
                "summary": null
            }
        @apiError (4xx) {Number} code The error code.
        """
        id = args[0]
        user = User()
        await user.connect()
        one = await user.select(id, 'nickname', 'email', 'avatar', 'gender', 'city', 'summary')
        del user
        if one is None:
            self.set_status(404)
            self.finish(Constant.user_not_exists)
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
        """
        @api {post} /user/:id Registration
        @apiVersion 0.1.0
        @apiName UserRegistration
        @apiGroup User
        @apiParam {String} password The password of the user.
        @apiParam {String} email The email of the user.
        @apiSuccess (201) {String} code The success code.
        @apiError (4xx) {Number} code The error code.
       """
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
        """
        @api {put} /user/:id Update user information
        @apiVersion 0.1.0
        @apiName UserUpdate
        @apiGroup User
        @apiPermission Authentication
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {String} [nickname] The nickname of the user.
        @apiParam {String} [password] The password of the user.
        @apiParam {String} [email] The email of the user.
        @apiParam {String} [avatar] The avatar url of the user.
        @apiParam {Number} [gender] The gender of the user, 0 is male, 1 is female.
        @apiParam {String} [String] city The city where user often lives.
        @apiParam {String} [String] summary The brief introduction of the user.
        @apiSuccess (200) {String} code The success code.
        @apiError (4xx) {Number} code The error code.
       """
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
