from abc import ABC

from apps.handlers import DefaultHandler, get_json, auth
from apps.label.model import Label
from apps.util.constant import Constant


class LabelHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        """
        @api {get} /label Get some labels, all labels in server default if article_id is not given
        @apiVersion 0.1.0
        @apiName UserGetAll
        @apiGroup Label
        @apiParam {Number} [article_id] JSON param, the id of this article, return this article's labels
        @apiSuccess (200) {Object[]} items The label name and its id array.
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "items": [
                    {
                    "id": 1,
                    "label": "Android"
                    },
                    {
                    "id": 2,
                    "label": "Java"
                    }
                ]
            }
        @apiError (404) {Number} code The error code.
        """
        la = Label()
        await la.connect()
        article_id = self.get_argument('article_id', None)
        if not article_id:
            many = await la.select_labels()
        else:
            many = await la.select_article_labels(int(article_id))
        if many is None or len(many) <= 0:
            self.set_status(404)
            self.finish(Constant.resource_not_exists)
            return
        labels = []
        for m in many:
            labels.append({
                'id': m[0],
                'label': m[1],
            })
        self.finish({'items': labels})

    @auth
    @get_json('label')
    async def post(self, *args, **kwargs):
        """
        @api {post} /label Create a label
        @apiVersion 0.1.0
        @apiName UserCreate
        @apiGroup Label
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {string} label JSON param, the label name
        @apiSuccess (201) {Number} id The created label id.
        @apiError (400) {Number} code The error code.
        """
        label = self.body.get('label')
        la = Label()
        await la.connect()
        one = await la.insert_label(label)
        del label
        if one is None:
            self.set_status(400)
            self.finish(Constant.resource_exists)
            return
        self.set_status(201)
        self.finish({'id': one[0]})

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        """
        @api {put} /label/:id Update a label
        @apiVersion 0.1.0
        @apiName UserUpdate
        @apiGroup Label
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {string} label JSON param, the new label name
        @apiSuccess (200) {Number} code The successful code.
        @apiError (404) {Number} code The error code.
        """
        await self.put_one(Label(), *args, **kwargs)

    @auth
    async def delete(self, *args, **kwargs):
        """
        @api {delete} /label/:id Delete a label
        @apiVersion 0.1.0
        @apiName UserDelete
        @apiGroup Label
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (200) {Number} code The successful code.
        @apiError (404) {Number} code The error code.
        """
        await self.delete_one(Label(), *args, **kwargs)
