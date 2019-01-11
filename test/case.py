import json
import unittest

from test.base import BaseCase


class Case(BaseCase):

    def test_a_user_a_register(self):
        path = '/user'
        res = self.fetch(path, method='POST')
        self.assertEqual(400, res.status_code)

        data = {'password': '1234'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, res.status_code)

        data = {'password': '1234', 'email': 'doforce@126.net'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, res.status_code)

        data = {'password': '1234', 'email': 'doforce@126.com', 'id': 'Edgar'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(201, res.status_code)

    def test_a_user_b_login(self):
        path = '/auth'
        data = {'password': '1234'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, res.status_code)

        data = {'password': '12345', 'id': 'Edgar'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, res.status_code)

        data = {'password': '1234', 'id': 'edgar'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(404, res.status_code)

        data = {'password': '1234', 'id': 'Edgar'}
        res = self.fetch(path, method='POST', data=data)
        self.assertEqual(201, res.status_code)
        self.assertTrue('token' in res.json())
        self.token = res.json().get('token', '')

    def test_a_user_get(self):
        path = '/user'
        res = self.fetch(path)
        self.assertEqual(401, res.status_code)

        self.fetchToken()
        res = self.fetch(path, token=self.token)
        self.assertEqual(200, res.status_code)
        self.assertTrue('nickname' in res.json())

        res = self.fetch(path, token=self.token, params={'check': 'y'})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, token=self.token, params={'check': 'y', 'id': 'd'})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, token=self.token, params={'check': 'y', 'id': 'Edgar'})
        self.assertEqual(200, res.status_code)

    def test_a_user_put(self):
        self.fetchToken()
        path = '/user'
        data = {'email': 'dddd', 'nickname': 'superman'}
        res = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(400, res.status_code)

        data = {'nickname': 'superman '}
        res = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(200, res.status_code)

        res = self.fetch(path, token=self.token)
        self.assertEqual(200, res.status_code)
        self.assertTrue('nickname' in res.json())
        nickname = res.json().get('nickname', '')
        self.assertTrue('Edgar' != nickname)

        data = {'nickname': 'Edgar'}
        res = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(200, res.status_code)

    def test_b_alabel_a_post(self):
        self.fetchToken()
        path = '/label'

        res = self.fetch(path, method='POST', data={'label': 'Android'})
        self.assertEqual(401, res.status_code)

        res = self.fetch(path, method='POST', data={'label': 'Android'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

        res = self.fetch(path, method='POST', data={'label': 'Android'}, token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path, method='POST', data={'label': 'Java'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

        res = self.fetch(path, method='POST', data={'label': 'Python'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

        res = self.fetch(path, method='POST', data={'label': 'Golang'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

        res = self.fetch(path, method='POST', data={'label': 'JavaScript'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

    def test_b_alabel_b_delete(self):
        self.fetchToken()
        path = '/label'
        res = self.fetch(path, method='POST', data={'label': 'Hello'}, token=self.token)
        self.assertEqual(201, res.status_code)
        self.assertTrue('id' in res.json())

        res = self.fetch(path + '/100', token=self.token, method='DELETE')
        self.assertEqual(404, res.status_code)

        res = self.fetch(path + '/7', token=self.token, method='DELETE')
        self.assertEqual(200, res.status_code)

        res = self.fetch(path + '/7', token=self.token, method='DELETE')
        self.assertEqual(404, res.status_code)

    def test_b_article_a_post(self):
        self.fetchToken()
        path = '/article'
        res = self.fetch(path, method='POST')
        self.assertEqual(401, res.status_code)

        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, res.status_code)

        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                'labels': ['Android', 'Python', 'Java']}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(400, res.status_code)

        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                'labels': [1, 4, 3]}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, res.status_code)
        for i in range(51):
            data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                    'labels': [1, 4, 3]}
            res = self.fetch(path, method='POST', token=self.token, data=data)
            self.assertEqual(201, res.status_code)
        for i in range(51):
            data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                    'labels': [4, 5, 6]}
            res = self.fetch(path, method='POST', token=self.token, data=data)
            self.assertEqual(201, res.status_code)

    def test_b_article_b_get(self):
        path = '/article'
        self.fetchToken()
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, res.status_code)
        id = res.json()['id']

        res = self.fetch(path, params={'article_id': 123456})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'article_id': id})
        self.assertEqual(200, res.status_code)
        self.assertTrue('title' in res.json()['items'][0])

        res = self.fetch(path)
        self.assertEqual(200, res.status_code)
        self.assertEqual(10, len(res.json()['items']))
        self.assertEqual(1, res.json()['items'][0]['id'])
        self.assertEqual(10, res.json()['items'][9]['id'])

        res = self.fetch(path, params={'start': 10})
        self.assertEqual(200, res.status_code)
        self.assertEqual(10, len(res.json()['items']))
        self.assertEqual(11, res.json()['items'][0]['id'])
        self.assertEqual(20, res.json()['items'][9]['id'])

        res = self.fetch(path, params={'start': 20, 'limit': 20})
        self.assertEqual(200, res.status_code)
        self.assertEqual(20, len(res.json()['items']))
        self.assertEqual(21, res.json()['items'][0]['id'])
        self.assertEqual(40, res.json()['items'][19]['id'])

        res = self.fetch(path, params={'limit': 500})
        self.assertEqual(200, res.status_code)
        self.assertNotEqual(500, len(res.json()['items']))

        res = self.fetch(path, params={'limit': 20, 'label_id': 10})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'limit': 20, 'label': 1})
        self.assertEqual(200, res.status_code)
        self.assertEqual(20, len(res.json()['items']))

    def test_b_article_c_put(self):
        self.fetchToken()
        path = '/article'
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, res.status_code)
        id = res.json()['id']

        res = self.fetch(path + '/1', method='PUT')
        self.assertEqual(401, res.status_code)

        res = self.fetch(path + '/23333', method='PUT', token=self.token)
        self.assertEqual(400, res.status_code)

        data = {'title': 'Hello world!'}
        res = self.fetch(path + '/{0}'.format(id), method='PUT', token=self.token, data=data)
        self.assertEqual(200, res.status_code)

        res = self.fetch(path + '/23333', method='PUT', token=self.token, data=data)
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'article_id': id})
        self.assertEqual(200, res.status_code)
        self.assertTrue('Hello world!' == res.json()['items'][0]['title'])

    def test_b_article_c_delete(self):
        self.fetchToken()
        path = '/article'
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        res = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, res.status_code)
        id = res.json()['id']

        res = self.fetch(path + '/231212', method='DELETE')
        self.assertEqual(401, res.status_code)

        res = self.fetch(path + '/231212', method='DELETE', token=self.token)
        self.assertEqual(404, res.status_code)

        res = self.fetch(path + '/{0}'.format(id), method='DELETE', token=self.token)
        self.assertEqual(200, res.status_code)
        res = self.fetch(path, params={'article_id': id})
        self.assertEqual(404, res.status_code)

    def test_b_article_f_bind_label(self):
        self.fetchToken()
        path = '/article/{0}/label/{1}'

        res = self.fetch(path.format(1000, 1), method='POST')
        self.assertEqual(401, res.status_code)

        res = self.fetch(path.format(1000, 1), method='POST', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 1000), method='POST', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 1), method='POST', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 6), method='POST', token=self.token)
        self.assertEqual(200, res.status_code)

        res = self.fetch(path.format(10, 1), method='POST', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 1), method='POST', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(1000, 1), method='DELETE', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 1), method='DELETE', token=self.token)
        self.assertEqual(200, res.status_code)

        res = self.fetch(path.format(10, 1), method='DELETE', token=self.token)
        self.assertEqual(400, res.status_code)

        res = self.fetch(path.format(10, 1), method='POST', token=self.token)
        self.assertEqual(200, res.status_code)

    def test_b_blabel_get(self):
        path = '/label'
        res = self.fetch(path)
        self.assertEqual(200, res.status_code)
        self.assertTrue(len(res.json()['items']) > 0)

        res = self.fetch(path, params={'article_id': 10000})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'article_id': 10})
        self.assertEqual(200, res.status_code)
        self.assertTrue(len(res.json()['items']) > 0)

    def test_c_comment_a_post(self):
        self.fetchToken()
        path = "/comment"
        data = {'article_id': 1000, 'content': self.cn_fake.text()}
        res = self.fetch(path, data=data, token=self.token, method='POST')
        self.assertEqual(400, res.status_code)

        data = {'article_id': 1, 'content': self.cn_fake.text()}
        res = self.fetch(path, data=data, token=self.token, method='POST')
        self.assertEqual(201, res.status_code)

        for i in range(2, 60):
            data = {'article_id': i, 'content': self.cn_fake.text()}
            res = self.fetch(path, data=data, token=self.token, method='POST')
            self.assertEqual(201, res.status_code)

        for i in range(100):
            data = {'article_id': 10, 'content': self.cn_fake.text()}
            res = self.fetch(path, data=data, token=self.token, method='POST')
            self.assertEqual(201, res.status_code)

    def test_c_comment_b_get(self):
        path = "/comment"
        res = self.fetch(path, params={'comment_id': 4294967290})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'comment_id': 1})
        self.assertEqual(200, res.status_code)
        self.assertEqual(1, res.json()['items'][0]['id'])

        res = self.fetch(path, params={'article_id': 122323232})
        self.assertEqual(404, res.status_code)

        res = self.fetch(path, params={'article_id': 10, 'start': 10})
        self.assertEqual(200, res.status_code)
        self.assertTrue(len(res.json()['items']) == 10)

        res = self.fetch(path, params={'article_id': 10, 'start': 20, 'limit': 20})
        self.assertEqual(200, res.status_code)
        self.assertEqual(20, len(res.json()['items']))

        res = self.fetch(path, params={'article_id': 10, 'limit': 500})
        self.assertEqual(200, res.status_code)
        self.assertEqual(101, len(res.json()['items']))

    def test_c_comment_c_delete(self):
        self.fetchToken()
        path = "/comment/{0}"
        res = self.fetch(path.format(4294967290), token=self.token, method='DELETE')
        self.assertEqual(404, res.status_code)

        res = self.fetch(path.format(59), token=self.token, method='DELETE')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
