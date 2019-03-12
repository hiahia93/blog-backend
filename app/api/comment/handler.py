from abc import ABC
import time

from app.handlers import DefaultHandler, get_json, auth
from app.api.comment.model import Comment
from app.util.constant import Constant


class CommentHandler(DefaultHandler, ABC):

    @auth
    @get_json('article_id', 'content')
    async def post(self, *args, **kwargs):
        """
        @api {post} /comment Get some comments of a article
        @apiVersion 0.1.0
        @apiName CommentCreate
        @apiGroup Comment
        @apiParam {Number} article_id JSON param, the id of a article
        @apiParam {Number} content JSON param, a comment content
        @apiSuccess (201) status
        @apiError (404) {String} err The error message.
        """
        article_id = int(self.body.get('article_id'))
        content = self.body.get('content')
        comment = Comment()
        await comment.connect()
        count = await comment.insert_comment(article_id, content)
        del comment
        if count <= 0:
            self.set_status(400)
            self.finish(Constant.bad_request)
            return
        self.set_status(201)

    async def get(self, *args, **kwargs):
        """
        @api {get} /comment?comment_id=0&label_id=0&start=0&limit=10 Get some comments of a article, a specific comment default
        @apiVersion 0.1.0
        @apiName ArticleComments
        @apiGroup Comment
        @apiParam {Number} [comment_id] The id of a specific comment
        @apiParam {Number} [start=0] The begin page number of the comments
        @apiParam {Number} [limit=10] The count of the comments that will be returned
        @apiParam {Number} [article_id] The article id that the comments were on
        @apiSuccess (200) {Object[]} items the articles object array
        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "items": [
                    "id": 1,
                    "title": "Hello",
                    "content": "I am Edgar, welcome to my world.",
                    "views": 2333,
                    "created_at": 1546414975,
                    "updated_at": 1546414975,
                ]
            }
        @apiError (404) {String} err The error message.
        """
        comment_id = self.get_argument('comment_id', None)
        comment = Comment()
        await comment.connect()
        if comment_id:
            one = await comment.select(int(comment_id), 'id', 'article_id', 'content', 'created_at')
            many = [one] if one else []
        else:
            start = int(self.get_argument('start', -1))
            limit = int(self.get_argument('limit', -1))
            article_id = self.get_argument('article_id', None)
            if not article_id:
                self.set_status(400)
                self.finish(Constant.params_insufficiency)
                return
            many = await comment.select_article_comments(int(article_id), start, limit)
        del comment
        if many is None or len(many) == 0:
            self.set_status(404)
            self.finish(Constant.resource_not_exists)
            return
        comments = []
        for m in many:
            comments.append({
                'id': m[0],
                'article_id': m[1],
                'content': m[2],
                'created_at': time.mktime(m[3].timetuple())
            })
        self.finish({'items': comments})

    @auth
    async def delete(self, *args, **kwargs):
        """
        @api {delete} /comment/:id Delete a comment
        @apiVersion 0.1.0
        @apiName CommentDelete
        @apiGroup Comment
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (204) status
        @apiError (404) {String} err The error message.
        """
        await self.delete_one(Comment(), *args, **kwargs)