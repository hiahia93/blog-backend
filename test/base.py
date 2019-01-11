import json
import unittest

from faker import Faker
from requests import request

import test.common as common


class BaseCase(unittest.TestCase):
    base_url = 'http://localhost:8888/api'
    en_fake = Faker()
    cn_fake = Faker('zh_CN')
    token = ''

    @classmethod
    def setUpClass(cls):
        common.truncate_table()

    def fetchToken(self):
        data = {'password': '1234', 'id': 'Edgar'}
        response = self.fetch('/auth', method='POST', data=data)
        self.assertEqual(201, response.status_code)
        self.token = response.json().get('token', '')

    def fetch(self, path: str, params=None, data=None, method: str = 'GET', token=None):
        if method == 'GET':
            data = None
        headers = {'Content-Type': 'application/json'}
        if token is not None:
            headers['token'] = token
        return request(method, self.base_url + path, headers=headers, params=params, data=json.dumps(data))