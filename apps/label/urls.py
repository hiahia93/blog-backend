from apps.label.handler import LabelHandler, LabelsHandler

url = [
    ('/api/label/(\w+)', LabelHandler),
    ('/api/labels', LabelsHandler),
]