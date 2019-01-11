from apps.user.urls import url as user_url
from apps.article.urls import url as article_url
from apps.comment.urls import url as comment_url
from apps.label.urls import url as label_url
from .handlers import IndexHandler, AuthHandler

urls = [
    ('/', IndexHandler),
    ('/api/auth', AuthHandler),
]
urls += user_url
urls += article_url
urls += comment_url
urls += label_url
