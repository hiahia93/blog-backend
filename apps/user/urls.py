from .handler import LoginHandler, UserExistHandler, UserHandler

url = [
    ('/api/user/(\w+)/login', LoginHandler),
    ('/api/user/(\w+)/exists', UserExistHandler),
    ('/api/user/(\w+)', UserHandler),
]