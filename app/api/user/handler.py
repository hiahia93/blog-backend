from abc import ABC

from app import cf
from app.handlers import DefaultHandler, get_json, auth
from app.api.user.model import User
from app.util.encrypt import md5
from app.util.constant import Constant


class UserHandler(DefaultHandler, ABC):

    @auth
    async def get(self, *args, **kwargs):
        """
        @api {get} /user Get user information
        @apiVersion 0.1.0
        @apiName UserInfo
        @apiGroup User
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (200) {String} nickname The nickname of the user.
        @apiSuccess (200) {String} email The email of the user.
        @apiSuccess (200) {String} avatar The avatar url of the user.
        @apiSuccess (200) {Number} gender The gender of the user, 0 is male, 1 is female.
        @apiSuccess (200) {String} city The city where user often lives.
        @apiSuccess (200) {String} summary The brief introduction of the user.
        @apiError (404) {String} err The error message.
        """
        username = self.current_user
        user = User()
        await user.connect()
        one = await user.select(username, 'nickname', 'email', 'avatar', 'gender', 'city', 'summary')
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

    @get_json('id', 'password', 'email')
    async def post(self, *args, **kwargs):
        """
        @api {post} /user/:id Registration
        @apiVersion 0.1.0
        @apiName UserRegistration
        @apiGroup User
        @apiParam {String} id JSON param, the id of the user.
        @apiParam {String} password JSON param, the password of the user.
        @apiParam {String} email JSON param, the email of the user.
        @apiSuccess (201) status
        @apiError (400) {String} err The error message.
        """
        username = self.body.get('id')
        pwd = self.body.get('password')
        email = self.body.get('email')
        if email != cf.get('server', 'email'):
            self.set_status(400)
            self.finish(Constant.params_error)
            return
        user = User()
        await user.connect()
        count = await user.insert_user(username, md5(pwd), email)
        del user
        if count <= 0:
            self.set_status(400)
            self.finish(Constant.user_exists)
            return
        self.set_status(201)

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        """
        @api {put} /user Update user information
        @apiVersion 0.1.0
        @apiName UserUpdate
        @apiGroup User
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {String} [nickname] JSON param, the nickname of the user.
        @apiParam {String} [password] JSON param, the password of the user.
        @apiParam {String} [avatar] JSON param, the avatar url of the user.
        @apiParam {Number} [gender] JSON param, the gender of the user, 0 is male, 1 is female.
        @apiParam {String} [city] JSON param, the city where user often lives.
        @apiParam {String} [summary] JSON param, the brief introduction of the user.
        @apiSuccess (204) status
        @apiError (400) {String} err The error message.
        """
        id = self.current_user
        user = User()
        await user.connect()
        if 'email' in self.body:
            self.set_status(400)
            self.finish(Constant.params_error)
            return
        if 'password' in self.body:
            self.body['password'] = md5(self.body['password'])
        count = await user.update(id, self.body)
        if count <= 0:
            self.set_status(400)
            self.finish(Constant.bad_request)
            return
        self.set_status(204)


class UserExistsHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        """
        @api {get} /user/exists?id=john
        @apiVersion 0.1.0
        @apiName UserExists
        @apiGroup User

        @apiParam {String} id The username
        @apiSuccess (204) status
        @apiError (404) c
        """
        username = self.get_argument('id', None)
        user = User()
        await user.connect()
        one = await user.select(username)
        del user
        if one is None:
            self.set_status(404)
            self.finish(Constant.user_not_exists)
            return
        self.set_status(204)