from apps.article.handler import ArticleHandler, ArticleLabelHandler

url = [
    ('/api/article/(\d+)', ArticleHandler),
    ('/api/article', ArticleHandler),
    ('/api/article/(\d+)/label/(\d+)', ArticleLabelHandler),
]
