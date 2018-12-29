import unittest
import json
import asyncio

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
        BaseCase.truncate_table()

    @staticmethod
    def truncate_table():
        common.truncate_table()

    def setUp(self):
        self.fetchToken()

    def fetchToken(self):
        data = {'id': 'Edgar', 'password': '1234'}
        response = self.fetch('/login', method='POST', data=data)
        try:
            self.token = response.json().get('token', '')
        except:
            pass

    def fetch(self, path: str, params=None, data=None, method: str = 'GET', token=None):
        if method == 'GET':
            data = None
        headers = {'Content-Type': 'application/json'}
        if token is not None:
            headers['token'] = token
        return request(method, self.base_url + path, headers=headers, params=params, data=json.dumps(data))

    async def tmp_fetch(self, path: str, params=None, data=None, method: str = 'GET', token=None):
        return self.fetch(path, params, data, method, token)

    def afetch(self, path: str, params=None, data=None, method: str = 'GET', token=None):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.tmp_fetch(path, params, data, method, token))
