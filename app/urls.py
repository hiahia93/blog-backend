from app.api.user.url import url as user_url
from app.api.article.url import url as article_url
from app.api.comment.url import url as comment_url
from app.api.label.urls import url as label_url
from .handlers import IndexHandler, AuthHandler

urls = [
    ('/', IndexHandler),
    ('/api/auth', AuthHandler),
]
urls += user_url
urls += article_url
urls += comment_url
urls += label_url
