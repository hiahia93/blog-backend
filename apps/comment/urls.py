from apps.comment.handler import CommentHandler

url = [
    ('/api/comment/(\d+)', CommentHandler),
    ('/api/comment', CommentHandler),
]