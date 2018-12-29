from abc import ABC
import time
from apps.default_handler import DefaultHandler, get_json, auth
from apps.comment.model import Comment


class CommentHandler(DefaultHandler, ABC):

    @auth
    @get_json('article_id', 'content')
    async def post(self, *args, **kwargs):
        article_id = int(self.body.get('article_id'))
        content = self.body.get('content')
        comment = Comment()
        await comment.connect()
        count = await comment.insert_comment(article_id, content)
        del comment
        if count <= 0:
            self.set_status(400)
            return
        self.set_status(201)

    async def get(self, *args, **kwargs):
        id = int(args[0])
        comment = Comment()
        await comment.connect()
        one = await comment.select(id, 'id', 'article_id', 'content', 'created_at')
        del comment
        if one is None:
            self.set_status(404)
            return
        self.finish({
            'id': one[0],
            'article_id': one[1],
            'content': one[2],
            'created_at': time.mktime(one[3].timetuple()),
        })

    @auth
    async def delete(self, *args, **kwargs):
        await self.delete_one(Comment(), *args, **kwargs)



