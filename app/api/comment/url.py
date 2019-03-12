from app.api.comment.handler import CommentHandler

url = [
    ('/api/comment/(\d+)', CommentHandler),
    ('/api/comment', CommentHandler),
]