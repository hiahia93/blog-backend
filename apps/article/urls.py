from apps.article.handler import ArticleHandler, ArticleCommentsHandler \
    , ArticleLabelsHandler, ArticlesHandler, ArticleLabelHandler

url = [
    ('/api/article/(\d+)', ArticleHandler),
    ('/api/article', ArticleHandler),
    ('/api/article/(\d+)/comments', ArticleCommentsHandler),
    ('/api/article/(\d+)/labels', ArticleLabelsHandler),
    ('/api/articles', ArticlesHandler),
    ('/api/article/(\d+)/label/(\w+)', ArticleLabelHandler),
]
