from .handler import UserHandler, UserExistsHandler

url = [
    ('/api/user', UserHandler),
    ('/api/user/exists', UserExistsHandler),
]