import hashlib
import random


def md5(text):
    md = hashlib.md5()
    md.update(bytes(text, encoding='utf-8'))
    return md.hexdigest()
