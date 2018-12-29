import time
import unittest
import asyncio

from test.base import BaseCase


class Case(BaseCase):

    def test_a_user_a_register(self):
        id = 'Edgar'
        path = '/user/' + id
        response = self.fetch(path)
        self.assertEqual(401, response.status_code)

        response = self.fetch(path, method='POST')
        self.assertEqual(400, response.status_code)

        data = {'password': '1234'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, response.status_code)

        data = {'password': '1234', 'email': 'doforce@126.net'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, response.status_code)

        data = {'password': '1234', 'email': 'doforce@126.com'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(201, response.status_code)

    def test_a_user_b_login(self):
        path = '/login'
        data = {'id': 'edgar', 'password': '1234'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(404, response.status_code)

        data = {'id': 'Edgar', 'password': '12345'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(400, response.status_code)

        data = {'id': 'Edgar', 'password': '1234'}
        response = self.fetch(path, method='POST', data=data)
        self.assertEqual(201, response.status_code)
        self.assertTrue('token' in response.json())
        self.token = response.json().get('token', '')

    def test_a_user_exists(self):
        path = '/user/Edgar/exists'
        response = self.fetch(path)
        self.assertEqual(200, response.status_code)

        path = '/user/sun/exists'
        response = self.fetch(path)
        self.assertEqual(404, response.status_code)

    def test_a_user_get(self):
        path = '/user/Edgar'
        response = self.fetch(path)
        self.assertEqual(401, response.status_code)

        path = '/user/Edgars'
        response = self.fetch(path, token=self.token)
        self.assertEqual(404, response.status_code)

        path = '/user/Edgar'
        response = self.fetch(path, token=self.token)
        self.assertEqual(200, response.status_code)
        self.assertTrue('nickname' in response.json())

    def test_a_user_put(self):
        path = '/user/Edgar'
        data = {'email': 'dddd', 'nickname': 'superman'}
        response = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(400, response.status_code)

        data = {'nickname': 'superman '}
        response = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(200, response.status_code)

        response = self.fetch(path, token=self.token)
        self.assertEqual(200, response.status_code)
        self.assertTrue('nickname' in response.json())
        nickname = response.json().get('nickname', '')
        self.assertTrue('Edgar' != nickname)

        data = {'nickname': 'Edgar'}
        response = self.fetch(path, method='PUT', token=self.token, data=data)
        self.assertEqual(200, response.status_code)

    def test_b_article_a_post(self):
        path = '/article'
        response = self.fetch(path, method='POST')
        self.assertEqual(401, response.status_code)

        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        response = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, response.status_code)

        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(), 'labels': ['Android', 'Python', 'Java']}
        response = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, response.status_code)
        for i in range(51):
            data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                    'labels': ['Java', 'Golang', 'JavaScript']}
            response = self.fetch(path, method='POST', token=self.token, data=data)
            self.assertEqual(201, response.status_code)
        for i in range(51):
            data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text(),
                    'labels': ['Android', 'Python']}
            response = self.fetch(path, method='POST', token=self.token, data=data)
            self.assertEqual(201, response.status_code)

    def test_b_article_b_get(self):
        path = '/article'
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        response = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, response.status_code)
        id = response.json()['id']

        response = self.fetch(path + '/231212')
        self.assertEqual(404, response.status_code)

        response = self.fetch(path + '/{0}'.format(id))
        self.assertEqual(200, response.status_code)
        self.assertTrue('title' in response.json())

    def test_b_article_c_put(self):
        path = '/article'
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        response = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, response.status_code)
        id = response.json()['id']

        response = self.fetch(path + '/231212', method='PUT')
        self.assertEqual(401, response.status_code)

        response = self.fetch(path + '/231212', method='PUT', token=self.token)
        self.assertEqual(400, response.status_code)

        data = {'title': 'Hello world'}
        response = self.fetch(path + '/{0}'.format(id), method='PUT', token=self.token, data=data)
        self.assertEqual(200, response.status_code)
        response = self.fetch(path + '/{0}'.format(id))
        self.assertEqual(200, response.status_code)
        self.assertTrue('Hello world' == response.json()['title'])

    def test_b_article_c_delete(self):
        path = '/article'
        data = {'title': self.en_fake.name(), 'content': self.cn_fake.text() + self.cn_fake.text()}
        response = self.fetch(path, method='POST', token=self.token, data=data)
        self.assertEqual(201, response.status_code)
        id = response.json()['id']

        response = self.fetch(path + '/231212', method='DELETE')
        self.assertEqual(401, response.status_code)

        response = self.fetch(path + '/231212', method='DELETE', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path + '/{0}'.format(id), method='DELETE', token=self.token)
        self.assertEqual(200, response.status_code)
        response = self.fetch(path + '/{0}'.format(id))
        self.assertEqual(404, response.status_code)

    def test_b_article_d_articles(self):
        path = '/articles'
        response = self.fetch(path)
        self.assertEqual(200, response.status_code)
        self.assertEqual(10, len(response.json()['items']))
        self.assertEqual(1, response.json()['items'][0]['id'])
        self.assertEqual(10, response.json()['items'][9]['id'])

        response = self.fetch(path, params={'start': 10})
        self.assertEqual(200, response.status_code)
        self.assertEqual(10, len(response.json()['items']))
        self.assertEqual(11, response.json()['items'][0]['id'])
        self.assertEqual(20, response.json()['items'][9]['id'])

        response = self.fetch(path, params={'start': 20, 'limit': 20})
        self.assertEqual(200, response.status_code)
        self.assertEqual(20, len(response.json()['items']))
        self.assertEqual(21, response.json()['items'][0]['id'])
        self.assertEqual(40, response.json()['items'][19]['id'])

        response = self.fetch(path, params={'limit': 500})
        self.assertEqual(200, response.status_code)
        self.assertNotEqual(500, len(response.json()['items']))

        response = self.fetch(path, params={'limit': 20, 'label': 'love_you'})
        self.assertEqual(404, response.status_code)

        response = self.fetch(path, params={'limit': 20, 'label': 'Android'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(20, len(response.json()['items']))

    def test_b_article_e_labels(self):
        path = '/article/{0}/labels'
        response = self.fetch(path.format(1000))
        self.assertEqual(404, response.status_code)

        response = self.fetch(path.format(1))
        self.assertEqual(404, response.status_code)

        response = self.fetch(path.format(10))
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.json()['items']))
        self.assertIn('Java', response.json()['items'])

    def test_b_article_f_bind_label(self):
        path = '/article/{0}/label/{1}'

        response = self.fetch(path.format(1000, 'Android'), method='POST')
        self.assertEqual(401, response.status_code)

        response = self.fetch(path.format(1000, 'Android'), method='POST', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(10, 'Android'), method='POST', token=self.token)
        self.assertEqual(200, response.status_code)

        response = self.fetch(path.format(10, 'Android'), method='POST', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(10, 'Android'), method='POST', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(1000, 'Android'), method='DELETE', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(10, 'Androids'), method='DELETE', token=self.token)
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(10, 'Android'), method='DELETE', token=self.token)
        self.assertEqual(200, response.status_code)

        response = self.fetch(path.format(10, 'Android'), method='POST', token=self.token)
        self.assertEqual(200, response.status_code)

    def test_c_comment_a_post(self):
        path = "/comment"
        data = {'article_id': 1000, 'content': self.cn_fake.text()}
        response = self.fetch(path, data=data, token=self.token, method='POST')
        self.assertEqual(400, response.status_code)

        data = {'article_id': 1, 'content': self.cn_fake.text()}
        response = self.fetch(path, data=data, token=self.token, method='POST')
        self.assertEqual(201, response.status_code)

        for i in range(2, 60):
            data = {'article_id': i, 'content': self.cn_fake.text()}
            response = self.fetch(path, data=data, token=self.token, method='POST')
            self.assertEqual(201, response.status_code)

        for i in range(100):
            data = {'article_id': 10, 'content': self.cn_fake.text()}
            response = self.fetch(path, data=data, token=self.token, method='POST')
            self.assertEqual(201, response.status_code)

    def test_c_comment_b_get(self):
        path = "/comment/{0}"
        response = self.fetch(path.format(4294967290))
        self.assertEqual(404, response.status_code)

        response = self.fetch(path.format(1))
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['id'])

    def test_c_comment_c_delete(self):
        path = "/comment/{0}"
        response = self.fetch(path.format(4294967290), token=self.token, method='DELETE')
        self.assertEqual(400, response.status_code)

        response = self.fetch(path.format(59), token=self.token, method='DELETE')
        self.assertEqual(200, response.status_code)

    def test_c_comment_c_article_comment(self):
        path = "/article/{0}/comments"
        response = self.fetch(path.format(4294967290))
        self.assertEqual(404, response.status_code)

        response = self.fetch(path.format(10), params={'start': 10})
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.json()['items']) == 10)

        response = self.fetch(path.format(10), params={'start': 20, 'limit': 20})
        self.assertEqual(200, response.status_code)
        self.assertEqual(20, len(response.json()['items']))

        response = self.fetch(path.format(10), params={'limit': 500})
        self.assertEqual(200, response.status_code)
        self.assertEqual(101, len(response.json()['items']))


if __name__ == '__main__':
    unittest.main()
