from .handler import UserHandler

url = [
    ('/api/user/(\w+)', UserHandler),
]