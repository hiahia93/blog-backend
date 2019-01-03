from apps.label.handler import LabelHandler

url = [
    ('/api/label', LabelHandler),
    ('/api/label/(\d+)', LabelHandler),
]