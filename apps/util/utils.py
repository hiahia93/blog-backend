import random
from datetime import datetime

CODE_POOL = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']


def random_code(code_length=8):
    code = ""
    for i in range(0, code_length):
        ran = random.choice(CODE_POOL)
        code += ran
    return code


def to_dict(obj, *filter) -> dict:
    result = {}
    for a in dir(obj):
        if a in filter:
            continue
        if a.startswith('_') or a == 'metadata':
            continue
        v = getattr(obj, a)
        if callable(v):
            continue
        if isinstance(v, datetime):
            v = v.strftime('%Y-%m-%d %H:%M:%S')
        result[a] = v
    return result