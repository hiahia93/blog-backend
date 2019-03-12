from abc import ABC
import time

from app.handlers import DefaultHandler, get_json, auth
from app.api.article.model import Article
from app.api.label.model import Label
from app.util.constant import Constant
from app.util.utils import list_all_type


class ArticleHandler(DefaultHandler, ABC):

    @auth
    @get_json('title', 'content', 'public')
    async def post(self, *args, **kwargs):
        """
        @api {post} /article Create an article
        @apiVersion 0.1.0
        @apiName ArticleCreate
        @apiGroup Article
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {string} title The title of the article
        @apiParam {string} content The content of the article
        @apiParam {Number} public whether the article is public
        @apiParam {Number[]} [labels] The label ids that will be binding the article
        @apiSuccess (201) {Number} id The created article id.
        @apiError (400) {String} err The error message.
        """
        title = self.body.get('title')
        content = self.body.get('content')
        public = self.body.get('public')
        article = Article()
        await article.connect()
        one = await article.insert_article(title, content, public)
        del article
        if one is None:
            self.set_status(400)
            self.finish(Constant.bad_request)
            return
        article_id = one[0]
        labels = self.body.get('labels')
        if 'labels' in self.body:
            if not isinstance(labels, list) or not list_all_type(labels, int):
                self.set_status(400)
                self.finish(Constant.params_error)
                return
            label = Label()
            await label.connect()
            await label.binding_labels(article_id, labels)
            del label
        self.set_status(201)
        self.finish({'id': article_id})

    async def get(self, *args, **kwargs):
        """
        @api {get} /article?article_id=0&start=0&limit=10&label_id=1 Get some articles, a specific article default
        @apiVersion 0.1.0
        @apiName Articles
        @apiGroup Article
        @apiParam {Number} [article_id] The id of this article, return this article's information
        @apiParam {Number} [start=0] The begin page number of the articles
        @apiParam {Number} [limit=10] The count of the articles that will be returned
        @apiParam {Number} [label_id] The label id that articles catch
        @apiSuccess (200) {Object[]} items the articles object array
        @apiSuccessExample {json} Success-Response:
             HTTP/1.1 200 OK
             {
                "items": [
                    "id": 1,
                    "title": "Hello",
                    "content": "I am Edgar, welcome to my world.",
                    "views": 2333,
                    "public": 1,
                    "created_at": 1546414975,
                    "updated_at": 1546414975,
                ]
             }
        @apiError (404) {String} err The error message.
        """

        start = int(self.get_argument('start', -1))
        limit = int(self.get_argument('limit', -1))
        label_id = self.get_argument('label_id', None)
        article_id = self.get_argument('article_id', None)
        article = Article()
        await article.connect()
        if article_id:
            one = await article.select(int(article_id), 'id', 'title', 'content', 'views', 'public', 'created_at', 'updated_at')
            many = [one] if one else []
        else:
            many = await article.select_articles(start, limit, label_id)
        del article
        if many is None or len(many) == 0:
            self.set_status(404)
            self.finish(Constant.resource_not_exists)
            return
        articles = []
        for m in many:
            articles.append({
                'id': m[0],
                'title': m[1],
                'content': m[2],
                'views': m[3],
                'public': m[4],
                'created_at': time.mktime(m[5].timetuple()),
                'updated_at': time.mktime(m[6].timetuple())
            })
        self.finish({'items': articles})

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        """
        @api {put} /article/:id Update an article
        @apiVersion 0.1.0
        @apiName ArticleUpdate
        @apiGroup Article
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiParam {string} [title] The new title of the article
        @apiParam {string} [content] The new content of the article
        @apiParam {Number} [public] whether the article is public
        @apiSuccess (204) status
        @apiError (404) {String} err The error message.
        """
        await self.put_one(Article(), *args, **kwargs)

    @auth
    async def delete(self, *args, **kwargs):
        """
        @api {delete} /article/:id Delete an article
        @apiVersion 0.1.0
        @apiName ArticleDelete
        @apiGroup Article
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (204) status
        @apiError (404) {String} err The error message.
        """
        await self.delete_one(Article(), *args, **kwargs)


class ArticleLabelHandler(DefaultHandler, ABC):

    @auth
    async def post(self, *args, **kwargs):
        """
        @api {post} /article/:article_id/label/:label_id Tag an article
        @apiVersion 0.1.0
        @apiName ArticleTag
        @apiGroup Article
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (204) status
        @apiError (400) {String} err The error message.
        """
        await self.handle(True, *args)

    @auth
    async def delete(self, *args, **kwargs):
        """
        @api {delete} /article/:article_id/label/:label_id Delete a label for an article
        @apiVersion 0.1.0
        @apiName ArticleUnTag
        @apiGroup Article
        @apiPermission Authorized
        @apiHeader {String} token The access token.
        @apiHeaderExample {json} Header-Example:
        {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0"
        }
        @apiSuccess (204) status
        @apiError (400) {String} err The error message.
        """
        await self.handle(False, *args)

    async def handle(self, insert: bool, *args):
        article_id = int(args[0])
        label_id = int(args[1])
        article = Article()
        await article.connect()
        count = await article.handle_article_label(article_id, label_id, insert)
        if count <= 0:
            self.set_status(400)
            return
        self.set_status(204)
