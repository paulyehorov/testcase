import flaskapp
import unittest
import json

class FlaskappTestCase(unittest.TestCase):

    def setUp(self):
        flaskapp.app.config['TESTING'] = True
        flaskapp.app.config['MONGODB_SETTINGS'] = { 'db': 'testcase-flask'}
        self.app = flaskapp.app.test_client()

    def tearDown(self):
        pass

    def testPostCorrect(self):
        data=json.dumps({
            "uid": "1",
            "name": "John Doe",
            "date": "2015-05-12T14:36:00.451765",
            "md5checksum": "a348be89b2fa602a9dc4713b245e1f1d"})
        resp = self.app.post('/post', data=data, content_type='application/json')
        assert 'saved' in resp.data

    def testPostWrong(self):
        data=json.dumps({
            "uid": "1",
            "name": "John Doe",
            "date": "2015-05-12T14:36:00.451765",
            "md5checksum": "a348be89b2fa602a9dc4713b245e1f1s"})
        resp = self.app.post('/post', data=data, content_type='application/json')
        assert 'MD5' in resp.data

    def testGetCorrect(self):
        data=json.dumps({
            "uid": "1",
            "name": "John Doe",
            "date": "2015-05-12T14:36:00.451765",
            "md5checksum": "a348be89b2fa602a9dc4713b245e1f1d"})
        resp = self.app.get('/get', data=data, content_type='application/json')
        assert '0' not in resp.data

    def testGetWrong(self):
        data=json.dumps({
            "uid": "2",
            "name": "John Doe",
            "date": "2015-05-12T14:36:00.451765",
            "md5checksum": "a348be89b2fa602a9dc4713b245e1f1d"})
        resp = self.app.get('/get', data=data, content_type='application/json')
        assert '0' in resp.data


if __name__ == '__main__':
    unittest.main()
