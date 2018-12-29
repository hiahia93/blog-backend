from abc import ABC
import time
from apps.default_handler import DefaultHandler, get_json, auth
from apps.article.model import Article
from apps.comment.model import Comment
from apps.label.model import Label


class ArticleHandler(DefaultHandler, ABC):

    @auth
    @get_json('title', 'content')
    async def post(self, *args, **kwargs):
        title = self.body.get('title')
        content = self.body.get('content')
        article = Article()
        await article.connect()
        one = await article.insert_article(title, content)
        del article
        if one is None:
            self.set_status(400)
            return
        article_id = one[0]
        if 'labels' in self.body and isinstance(self.body['labels'], list):
            label = Label()
            await label.connect()
            await label.binding_labels(article_id, self.body.get('labels'))
            del label
        self.set_status(201)
        self.finish({'id': article_id})

    async def get(self, *args, **kwargs):
        id = int(args[0])
        article = Article()
        await article.connect()
        one = await article.select(id, 'id', 'title', 'content', 'views', 'created_at', 'updated_at')
        del article
        if one is None:
            self.set_status(404)
            return
        self.finish({
            'id': one[0],
            'title': one[1],
            'content': one[2],
            'views': one[3],
            'created_at': time.mktime(one[4].timetuple()),
            'updated_at': time.mktime(one[5].timetuple())
        })

    @auth
    @get_json()
    async def put(self, *args, **kwargs):
        await self.put_one(Article(), *args, **kwargs)

    @auth
    async def delete(self, *args, **kwargs):
        await self.delete_one(Article(), *args, **kwargs)


class ArticlesHandler(DefaultHandler, ABC):
    async def get(self, *args, **kwargs):
        start = int(self.get_argument('start', -1))
        limit = int(self.get_argument('limit', -1))
        label = self.get_argument('label', '')
        article = Article()
        await article.connect()
        many = await article.select_articles(start, limit, label)
        del article
        if many is None or len(many) == 0:
            self.set_status(404)
            return
        articles = []
        for m in many:
            articles.append({
                'id': m[0],
                'title': m[1],
                'content': m[2],
                'views': m[3],
                'created_at': time.mktime(m[4].timetuple()),
                'updated_at': time.mktime(m[5].timetuple())
            })
        self.finish({'items': articles})


class ArticleCommentsHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        id = int(args[0])
        start = int(self.get_argument('start', -1))
        limit = int(self.get_argument('limit', -1))
        comment = Comment()
        await comment.connect()
        many = await comment.select_article_comments(id, start, limit)
        del comment
        if many is None or len(many) == 0:
            self.set_status(404)
            return
        comments = []
        for m in many:
            comments.append({
                'id': m[0],
                'content': m[1],
                'created_at': time.mktime(m[2].timetuple())
            })
        self.finish({'items': comments})


class ArticleLabelsHandler(DefaultHandler, ABC):

    async def get(self, *args, **kwargs):
        id = int(args[0])
        label = Label()
        await label.connect()
        many = await label.select_article_labels(id, 'label')
        del label
        if many is None or len(many) == 0:
            self.set_status(404)
            return
        labels = []
        for m in many:
            labels.append(m[0])
        self.finish({'items': labels})


class ArticleLabelHandler(DefaultHandler, ABC):

    @auth
    async def post(self, *args, **kwargs):
        await self.handle(True, *args)

    @auth
    async def delete(self, *args, **kwargs):
        await self.handle(False, *args)

    async def handle(self, insert: bool, *args):
        article_id = args[0]
        label = args[1]
        article = Article()
        await article.connect()
        count = await article.handle_article_label(article_id, label, insert)
        if count <= 0:
            self.set_status(400)
            return
